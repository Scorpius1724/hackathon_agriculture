import os
import glob

def find_filepath(upload_folder):
    image_files = glob.glob(os.path.join(upload_folder, '*'))

    if not image_files:
        print("No images found in the upload folder.")
        return None

    latest_image = max(image_files, key=os.path.getctime)

    return latest_image
