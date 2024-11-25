import os
import time
import csv
from termcolor import colored
import sys
from pathlib import Path

# File to store the hidden Telegram groups and channels
BASE_DIR = Path(__file__).resolve().parent
FILE_NAME = BASE_DIR / "hidden_crypto_groups.txt"
BACKUP_FILE_NAME = BASE_DIR / "hidden_crypto_groups_backup.txt"

def initialize_file():
    """Initialize the file if it doesn't exist."""
    if not FILE_NAME.exists():
        with open(FILE_NAME, 'w') as file:
            file.write("# Hidden Crypto Groups and Channels on Telegram\n")

# Rest of the code remains the same, making sure to use FILE_NAME and BACKUP_FILE_NAME appropriately.




def initialize_file():
    """Initialize the file if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as file:
            file.write("# Hidden Crypto Groups and Channels on Telegram\n")

def animate_banner(banner_lines, delay=0.05):
    """Animate the red banner line by line."""
    skip_animation = input("Do you want to skip the banner animation? (y/n): ").strip().lower()
    if skip_animation == 'y':
        return
    for line in banner_lines:
        sys.stdout.write(colored(line + "\n", "red", attrs=["bold"]))
        sys.stdout.flush()
        time.sleep(delay)

def add_group_or_channel():
    """Add a new hidden crypto group or channel to the file."""
    name = input("Enter the name of the group or channel: ")
    description = input("Enter a short description: ")
    link = input("Enter the Telegram link: ")
    
    with open(FILE_NAME, 'a') as file:
        file.write(f"Name: {name}\nDescription: {description}\nLink: {link}\n\n")
    print("Group or channel added successfully!\n")

def search_group_or_channel():
    """Search for a hidden crypto group or channel by name."""
    search_query = input("Enter the name or keyword to search: ").lower()
    
    found = False
    with open(FILE_NAME, 'r') as file:
        for group in file:
            if group.strip() == "":
                continue
            if search_query in group.lower():
                print("\nFound Group or Channel:\n")
                print(group)
                found = True
                break
    
    if not found:
        print("\nNo matching group or channel found.\n")

def view_all_groups():
    """View all saved groups and channels."""
    with open(FILE_NAME, 'r') as file:
        print("\nAll Saved Groups and Channels:\n")
        for line in file:
            if line.strip() != "":
                print(line, end='')
        print()

def delete_group_or_channel():
    """Delete a group or channel by name."""
    search_query = input("Enter the name or keyword of the group or channel to delete: ").lower()
    
    found = False
    updated_groups = []
    with open(FILE_NAME, 'r') as file:
        for group in file:
            if group.strip() == "":
                continue
            if search_query in group.lower():
                found = True
            else:
                updated_groups.append(group)
    
    with open(FILE_NAME, 'w') as file:
        for group in updated_groups:
            file.write(group + '\n')
    
    if found:
        print("\nGroup or channel deleted successfully.\n")
    else:
        print("\nNo matching group or channel found.\n")

def edit_group_or_channel():
    """Edit the information of a saved group or channel."""
    search_query = input("Enter the name or keyword of the group or channel to edit: ").lower()
    
    found = False
    updated_groups = []
    with open(FILE_NAME, 'r') as file:
        for group in file:
            if group.strip() == "":
                continue
            if search_query in group.lower():
                print("\nCurrent Group or Channel Information:\n")
                print(group)
                name = input("Enter the new name of the group or channel: ")
                description = input("Enter the new description: ")
                link = input("Enter the new Telegram link: ")
                updated_groups.append(f"Name: {name}\nDescription: {description}\nLink: {link}\n")
                found = True
            else:
                updated_groups.append(group)
    
    with open(FILE_NAME, 'w') as file:
        for group in updated_groups:
            file.write(group + '\n')
    
    if found:
        print("\nGroup or channel updated successfully.\n")
    else:
        print("\nNo matching group or channel found.\n")

def backup_data():
    """Create a backup of the saved groups and channels."""
    with open(FILE_NAME, 'r') as original_file:
        with open(BACKUP_FILE_NAME, 'w') as backup_file:
            backup_file.write(original_file.read())
    print(f"\nBackup created successfully as {BACKUP_FILE_NAME}.")

def sort_groups_and_channels():
    """Sort the saved groups and channels alphabetically by name."""
    groups = []
    with open(FILE_NAME, 'r') as file:
        for group in file:
            if group.strip() != "":
                groups.append(group)
    
    try:
        groups.sort(key=lambda x: x.split('\n')[0].lower())
    except IndexError:
        print("\nError: One or more groups are missing expected fields and could not be sorted.")
        return
    
    with open(FILE_NAME, 'w') as file:
        for group in groups:
            file.write(group + '\n')
    print("\nGroups and channels sorted successfully.")

def export_to_csv():
    """Export the saved groups and channels to a CSV file."""
    csv_file_name = "hidden_crypto_groups.csv"
    groups = []
    with open(FILE_NAME, 'r') as file:
        for group in file:
            if group.strip() != "":
                groups.append(group)
    
    try:
        with open(csv_file_name, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Description', 'Link']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for group in groups:
                lines = group.split('\n')
                if len(lines) >= 3:
                    name = lines[0].replace("Name: ", "").strip()
                    description = lines[1].replace("Description: ", "").strip()
                    link = lines[2].replace("Link: ", "").strip()
                    writer.writerow({'Name': name, 'Description': description, 'Link': link})
        print(f"\nData exported successfully to {csv_file_name}.")
    except (IOError, csv.Error) as e:
        print(f"\nError exporting to CSV: {e}")

def main():
    """Main function to run the script."""
    # Banner lines to display
    banner_lines = [
        "█████╗ ██╗  ██╗███╗   ███╗ █████╗ ██████╗     ████████╗███████╗ ██████╗██╗  ██╗    ██╗   ██╗██████╗ ",
        "██╔══██╗██║  ██║████╗ ████║██╔══██╗██╔══██╗    ╚══██╔══╝██╔════╝██╔════╝██║  ██║    ██║   ██║╚════██╗",
        "███████║███████║██╔████╔██║███████║██║  ██║       ██║   █████╗  ██║     ███████║    ██║   ██║ █████╔╝",
        "██╔══██║██╔══██║██║╚██╔╝██║██╔══██║██║  ██║       ██║   ██╔══╝  ██║     ██╔══██║    ╚██╗ ██╔╝██╔═══╝ ",
        "██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║██████╔╝       ██║   ███████╗╚██████╗██║  ██║     ╚████╔╝ ███████╗",
        "╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝        ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝      ╚═══╝  ╚══════╝",
        "                                                                                                     "
    ]
    
    # Display animated banner and notice
    animate_banner(banner_lines)
    print("\nWARNING: You use this tool at your own risk. The creator is not responsible for any misuse or consequences that arise from using this tool.\n")
    
    initialize_file()
    
    while True:
        print("\nMenu:")
        print("1. Add a new hidden crypto group or channel")
        print("2. Search for a hidden crypto group or channel")
        print("3. View all saved groups and channels")
        print("4. Delete a group or channel")
        print("5. Edit a group or channel")
        print("6. Backup data")
        print("7. Sort groups and channels")
        print("8. Export groups and channels to CSV")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            add_group_or_channel()
        elif choice == '2':
            search_group_or_channel()
        elif choice == '3':
            view_all_groups()
        elif choice == '4':
            delete_group_or_channel()
        elif choice == '5':
            edit_group_or_channel()
        elif choice == '6':
            backup_data()
        elif choice == '7':
            sort_groups_and_channels()
        elif choice == '8':
            export_to_csv()
        elif choice == '9':
            print("Exiting... Goodbye!")
            break
        else
