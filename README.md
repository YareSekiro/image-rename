# Image File Organizer

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Use](#how-to-use)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Description

The Image File Organizer is a Python script designed to help you efficiently manage and organize your image files in a specific directory. This script scans a given folder path, renames the image files based on the folder structure, and provides various functionalities to list and manage the images.

## Features

- **File Renaming:** The script automatically renames image files in the specified folder and its subfolders. The new names are composed of the folder names and an index to ensure uniqueness.

- **Listing Images:** The script offers two listing options:
  - `list:all`: Lists all image files in the specified directory and its subdirectories.
  - `list:folder`: Lists the folder names and their children folders (if any) where images are present.

- **Organizing Images:** The script maintains a dictionary with statistics about the number of image files in each folder and its children folders, effectively organizing your images based on their folder structure.

## Getting Started

### Prerequisites

To run the Image File Organizer, ensure that you have the following installed on your system:

- Python (version X.X.X)
- [List any other prerequisites if required]

### Installation

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

## How To Use

1. Set the folder_path variable at the beginning of the script to the path where you want to organize your images.
2. Run the script with the desired command. The available commands are:
3. list:all: To list all image files in the specified folder and its subfolders.
4. list:folder: To list the folder names and their children folders where images are present.
5. rename:all: To rename all image files in the specified folder and its subfolders.
6. The script will prompt you to enter a valid command if no command is provided as a command-line argument.

For the rename:all command, the script first renames the files with temporary names (e.g., "Temp_1.gif") and then renames them with the final names (e.g., "Sasuke_1.gif"). This ensures that file name clashes are avoided.
