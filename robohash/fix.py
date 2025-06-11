from PIL import Image
import os

def aggressive_fix_all_images(folder_path):
    problem_files = []
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.png') and not file.startswith('temp_'):
                filepath = os.path.join(root, file)
                try:
                    img = Image.open(filepath)
                    
                    # Force convert ALL images to clean RGBA, regardless of current mode
                    print(f"Processing {file} (Mode: {img.mode})")
                    
                    # Create a new clean RGBA image
                    new_img = Image.new('RGBA', img.size, (0, 0, 0, 0))
                    
                    # Convert source to RGBA first
                    if img.mode != 'RGBA':
                        if img.mode == 'P':
                            # Handle palette images specially
                            img = img.convert('RGBA')
                        elif img.mode in ['RGB', 'L', 'LA']:
                            img = img.convert('RGBA')
                    
                    # Paste onto clean background
                    new_img.paste(img, (0, 0), img)
                    
                    # Save without any optimization that might cause issues
                    new_img.save(filepath, 'PNG', optimize=False, compress_level=1)
                    print(f"  ✓ Fixed {file}")
                    
                except Exception as e:
                    print(f"  ❌ Error with {file}: {e}")
                    problem_files.append(filepath)
    
    if problem_files:
        print("\nProblem files that couldn't be fixed:")
        for f in problem_files:
            print(f"  {f}")
    else:
        print("\n✓ All files processed successfully!")

# Run the aggressive fix
aggressive_fix_all_images("C:/code/Robohash/robohash/sets/set6")