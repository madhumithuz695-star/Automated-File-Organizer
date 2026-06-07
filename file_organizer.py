import os
import shutil

# Organize panna vendiya folder path
folder_path = input("Enter folder path: ")

# File types
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

# Folder exists ah check
if not os.path.exists(folder_path):
    print("Folder not found!")
    exit()

# Files organize
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()

        moved = False

        for folder_name, extensions in file_types.items():
            if extension in extensions:
                target_folder = os.path.join(folder_path, folder_name)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(file_path, os.path.join(target_folder, file))
                print(f"Moved: {file} -> {folder_name}")
                moved = True
                break

        if not moved:
            others_folder = os.path.join(folder_path, "Others")

            if not os.path.exists(others_folder):
                os.makedirs(others_folder)

            shutil.move(file_path, os.path.join(others_folder, file))
            print(f"Moved: {file} -> Others")

print("File organization completed successfully!")
