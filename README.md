# 🗂️ File Organizer Script

This script is a simple yet effective Python utility designed to automatically organize files within a specified directory (typically a "Random" or Downloads folder). It categorizes files based on their extensions and moves them into corresponding subdirectories, such as Images, Videos, Audio, Documents, and Archives. This helps maintain a clean and organized file system, saving time and effort in manually sorting files.

## 🚀 Key Features

- **Automated File Categorization:** Automatically sorts files into predefined categories based on their file extensions.
- **Directory Organization:** Moves files into dedicated subdirectories for each category (Images, Videos, Audio, Documents, Archives, Others).
- **Simple Configuration:**  Easy to configure the target directory and destination subdirectories.
- **Cross-Platform Compatibility:** Works on any operating system that supports Python.
- **Easy to Use:** Simple script that can be run from the command line or scheduled for automated execution.

## 🛠️ Tech Stack

*   **Programming Language:** Python
*   **Core Libraries:**
    *   `os`:  Operating system interface for interacting with the file system.
    *   `pathlib`: Object-oriented file path handling.
    *   `shutil`: High-level file operations (moving files).

## 📦 Getting Started

### Prerequisites

- Python 3.6 or higher installed on your system.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **No additional packages are required.** The script uses built-in Python modules.

### Running Locally

1.  **Modify the script (optional):**
    *   Edit the `organizer.py` file to set the `folder_path` variable to the directory you want to organize.
    *   Adjust the `pic_path`, `vid_path`, `aud_path`, `doc_path`, `arc_path`, and `others` variables to specify the desired destination subdirectories.  Ensure these directories exist, or the script will throw an error.

2.  **Run the script:**

    ```bash
    python organizer.py
    ```

    This will organize the files in the specified directory.

## 📂 Project Structure

```
.
├── organizer.py       # Main script for organizing files
└── README.md          # Documentation for the project
```

## 📸 Screenshots

| Before running organizer.py | After running organizer.py |
| :---: | :---: |
| <img src="screenshots/Screenshot 2025-11-17 180447.png" alt="Main Screen" width="350"/> | <img src="screenshots/Screenshot 2025-11-17 182201.png" alt="Secondary Feature" width="350"/> |

## 🤝 Contributing

Contributions are welcome! If you have any ideas for improvements or bug fixes, please submit a pull request.

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes.
4.  Submit a pull request.

## 📬 Contact

If you have any questions or issues, please feel free to contact me at zenabadnan10@gmail.com

## 💖 Thanks

Thank you for using the File Organizer Script! I hope it helps you keep your files organized.

