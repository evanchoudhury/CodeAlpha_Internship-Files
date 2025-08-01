import os
import shutil

def move_jpg_files(src_folder, dest_folder):
    """
    Moves all .jpg files from src_folder to dest_folder.
    Creates dest_folder if it does not exist.
    """
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"Created destination folder: {dest_folder}")

    files_moved = 0
    for filename in os.listdir(src_folder):
        if filename.lower().endswith('.jpg'):
            src_path = os.path.join(src_folder, filename)
            dest_path = os.path.join(dest_folder, filename)
            shutil.move(src_path, dest_path)
            print(f"Moved: {filename}")
            files_moved += 1

    print(f"Total .jpg files moved: {files_moved}")

if __name__ == "__main__":
    # Example usage - update these paths as needed
    source_folder = "source_folder"
    destination_folder = "destination_folder"
    move_jpg_files(source_folder, destination_folder)
