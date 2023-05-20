import os 

def list_directory_contents(directory):
    if os.path.exists(directory):
        print(f"Contents of directory '{directory}':")
        items = os.listdir(directory)
        for item in items:
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                print(f"File: {item}")

            elif os.path.isdir(item_path):
                print(f"Directory: \U0001F4C1 {item}")  # Folder icon

            else:
                print(f"Unknown item: {item}")

        else:
             print("Directory does not exist.")

def main():
    directory = input("Enter the directory path: ")
    list_directory_contents(directory)

if __name__ == '__main__':
    main()
        
