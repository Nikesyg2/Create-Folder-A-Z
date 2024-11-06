import os
import zipfile
import pyfiglet
from colorama import init, Fore

init(autoreset=True)

def watermark():
    watermark_text = "This code created by Nikesyg"
    ascii_art = pyfiglet.figlet_format(watermark_text)
    print(Fore.CYAN + ascii_art)

def main():
    watermark()
    
    print(Fore.LIGHTCYAN_EX + "Do you want to create the folder in:")
    print(Fore.LIGHTCYAN_EX + "1. Android")
    print(Fore.LIGHTCYAN_EX + "2. Desktop")
    
    choice = input(Fore.LIGHTCYAN_EX + "Please enter your choice (1/2): ")
    
    if choice == '1':
        output_directory = "/storage/emulated/0/Nikesyg/folder/done"
    elif choice == '2':
        output_directory = "C:/Nikesyg/folder/done"
    else:
        print(Fore.LIGHTCYAN_EX + "Invalid choice. Exiting...")
        return

    confirm = input(Fore.LIGHTCYAN_EX + "Do you want to create the folders now? (y/n): ").strip().lower()
    
    if confirm != 'y':
        print(Fore.LIGHTCYAN_EX + "Folder creation canceled.")
        return

    for char in range(ord('A'), ord('Z') + 1):
        folder_name = chr(char)
        folder_path = os.path.join(output_directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        print(Fore.LIGHTCYAN_EX + f"Folder {folder_name} created.")

    zip_file_path = os.path.join(output_directory, "A_to_Z.zip")
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for folder_name in range(ord('A'), ord('Z') + 1):
            folder_path = os.path.join(output_directory, chr(folder_name))
            zipf.write(folder_path, os.path.basename(folder_path))

    print(Fore.LIGHTCYAN_EX + f"Folders created and zipped at {zip_file_path}")

    print(Fore.LIGHTCYAN_EX + "See my tools and contact me:")
    print(Fore.LIGHTCYAN_EX + "🐙 GitHub: https://github.com/Nikesyg2")
    print(Fore.LIGHTCYAN_EX + "📱 WhatsApp: https://wa.me/6281332383711")
    print(Fore.LIGHTCYAN_EX + "📸 Instagram: https://instagram.com/atanasius_reynaldi")

    print(Fore.LIGHTCYAN_EX + "You can request or recommended a tools too... :3")

if __name__ == "__main__":
    main()
