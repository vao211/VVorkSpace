
# VVorkSpace Beta

VVorkSpace Beta is a GUI application built with Python that allows users to easily add, manage, and launch other applications from a single window. It provides a friendly and simple interface to help users quickly access their favorite applications.

## Features

- **Add Applications**: Easily add applications or folders to your workspace.
- **Icon Management**: Customize icons for each application with optional images.
- **Launch Applications**: Quickly open applications from the main interface.
- **Startup Option**: Set the application to run automatically when Windows starts.
- **Change Resolution**: Adjust the application window size according to personal needs.
- **Fullscreen Mode**: Toggle between fullscreen and windowed mode.

## Requirements

- Python 3.x
- Required libraries:
  - `customtkinter`
  - `PIL`
  - `win32com`
  - `json`
  - `os`
  - `shutil`

## Installation

1. **Clone the Repository**:
   git clone https://github.com/vao211/VVorkSpace_Beta
   cd VVorkSpace_Beta

2. **Packaging with PyInstaller**:
    To create a standalone executable of the application, use PyInstaller with the following command:
    pyinstaller --onefile --noconsole --icon=icon/VVorkSpace.ico VVorkSpace_Beta.py