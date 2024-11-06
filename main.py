import os
import zipfile

# Specify the location where you want to create the folder.
output_directory = "C:/path/to/folder"  # Replace this path with your desired location
# Make folder "A" 'till "Z"
for char in range(ord('A'), ord('Z') + 1):
    folder_name = chr(char)
    folder_path = os.path.join(output_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder {folder_name} created.")

# Zip folder "A" 'till "Z" in one file
zip_file_path = os.path.join(output_directory, "A_to_Z.zip")
with zipfile.ZipFile(zip_file_path, 'w') as zipf:
    for folder_name in range(ord('A'), ord('Z') + 1):
        folder_path = os.path.join(output_directory, chr(folder_name))
        zipf.write(folder_path, os.path.basename(folder_path))

print(f"Folder created {zip_file_path}")

// Created by Nikesyg2
