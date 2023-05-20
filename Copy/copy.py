import os

import shutil 

def copy_file(src, dest):
    shutil.copy2(src, dest)

def copy_directory(src, dest):
    shutil.copy_tree(src, dest)

def main():
    source_path = input("Enter the source path: ")
    destination_path = input("Enter the destination_path: ")

    if os.path.isfile(source_path):
        destination = copy_file(source_path, destination_path)
        print(f"File copied successfully to {destination}")

    elif os.path.isdir(source_path):
        destination = copy_directory(source_path, destination_path)
        print("Directory copied successfully to {destination}")

    else:
        print("Source path does not exist")

if __name__ == '__main__':
    main()


        
