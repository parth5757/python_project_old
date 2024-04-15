import tkinter as tk
from tkinter import filedialog
import os

def list_folders(path, indent=0, output_file=None, ignore_folders=None):
    try:
        items = os.listdir(path)
    except PermissionError:
        return

    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            if item in ignore_folders:
                continue
            output_file.write('  ' * indent + f'[{item}]\n')
            list_folders(item_path, indent + 1, output_file, ignore_folders)
        else:
            output_file.write('  ' * indent + item + '\n')

def browse_folder_and_save():
    folder_path = filedialog.askdirectory(title="Select a folder")
    if folder_path:
        ignore_list = input("Enter folder names to ignore (separated by comma): ").split(",")
        ignore_list = [folder.strip() for folder in ignore_list]
        output_file_path = "folder_structure.txt"
        with open(output_file_path, "w") as output_file:
            output_file.write(f"Selected folder: {folder_path}\n")
            list_folders(folder_path, output_file=output_file, ignore_folders=ignore_list)
        print(f"Folder structure saved to {output_file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    print("Please select a folder using the file dialog.")
    browse_folder_and_save()
