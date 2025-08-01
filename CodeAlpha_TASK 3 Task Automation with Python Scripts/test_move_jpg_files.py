import os
import shutil
import tempfile
from move_jpg_files import move_jpg_files

def create_file(path):
    with open(path, 'w') as f:
        f.write("test")

def test_move_jpg_files():
    # Create temporary source and destination directories
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Create some test files in source directory
        create_file(os.path.join(src_dir, "image1.jpg"))
        create_file(os.path.join(src_dir, "image2.JPG"))  # uppercase extension
        create_file(os.path.join(src_dir, "document.txt"))
        create_file(os.path.join(src_dir, "photo.png"))

        # Remove the destination directory to test creation
        shutil.rmtree(dest_dir)

        # Run the function
        move_jpg_files(src_dir, dest_dir)

        # Check that destination directory was created
        assert os.path.exists(dest_dir), "Destination folder was not created"

        # Check that only .jpg files were moved
        moved_files = os.listdir(dest_dir)
        assert "image1.jpg" in moved_files, "image1.jpg not moved"
        assert "image2.JPG" in moved_files, "image2.JPG not moved"
        assert "document.txt" not in moved_files, "Non-jpg file moved"
        assert "photo.png" not in moved_files, "Non-jpg file moved"

        # Check that source directory no longer has the moved files
        remaining_files = os.listdir(src_dir)
        assert "image1.jpg" not in remaining_files, "image1.jpg still in source"
        assert "image2.JPG" not in remaining_files, "image2.JPG still in source"
        assert "document.txt" in remaining_files, "document.txt missing from source"
        assert "photo.png" in remaining_files, "photo.png missing from source"

        print("All tests passed.")

if __name__ == "__main__":
    test_move_jpg_files()
