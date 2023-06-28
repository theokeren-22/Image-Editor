from PIL import Image, ImageEnhance, ImageFilter
import os

input_dir = "./imgs"  # Folder for unedited images
output_dir = "./editedImgs"  # Folder for edited images

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# List comprehension to get input file paths
input_files = [os.path.join(input_dir, filename) for filename in os.listdir(input_dir)]

# Image editing operations
def edit_image(image):
    edit = image.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    # Adjust contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    return edit

# Process each input image
for input_path in input_files:
    try:
        with Image.open(input_path) as img:
            # Edit the image
            edited_img = edit_image(img)

            # Get the output file path
            output_filename = f"{os.path.splitext(os.path.basename(input_path))[0]}_edited.jpg"
            output_path = os.path.join(output_dir, output_filename)

            # Save the edited image
            edited_img.save(output_path)

            print(f"Image edited and saved: {output_filename}")
    except (IOError, OSError) as e:
        print(f"Error processing {input_path}: {e}")

print("Image editing completed.")
