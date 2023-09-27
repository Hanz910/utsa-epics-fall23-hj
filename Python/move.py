import os
import random

def distribute_images(source_folder, target_folders, images_per_folder):
    image_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f)) and not f.endswith('.py')]
    random.shuffle(image_files)

    for i, target_folder in enumerate(target_folders, start=1):
        os.makedirs(target_folder, exist_ok=True)
        images_to_move = image_files[(i - 1) * images_per_folder: i * images_per_folder]

        for image in images_to_move:
            source_path = os.path.join(source_folder, image)
            target_path = os.path.join(target_folder, image)
            os.rename(source_path, target_path)
            print(f"Moved {image} to {target_folder}")

if __name__ == "__main__":
    source_folder = r"C:\Users\lilia\OneDrive\Escritorio\EPICS Fall 2023"
    target_folders = ["folder1", "folder2", "folder3", "folder4", "folder5"]
    images_per_folder = 10  # Adjust this based on the number of images you want in each folder

    distribute_images(source_folder, target_folders, images_per_folder)
