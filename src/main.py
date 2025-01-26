#!/usr/bin/env python3

import os
from datetime import datetime

def main():
    # Define the folder and file path
    folder_path = "/repo/version-control"  # Update this with your actual folder path
    file_name = "version.md"
    file_path = os.path.join(folder_path, file_name)

    # Get current date and time
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Write to file
    with open(file_path, 'w') as file:
        file.write(current_datetime)

    print(f"Current date and time ({current_datetime}) written to {file_path}")

if __name__ == "__main__":
    main()

