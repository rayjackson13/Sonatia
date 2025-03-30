# Sonatia Project 🎵
**Sonatia** is a Python-based desktop application designed to streamline the management of music projects. Whether you're organizing tracks, mixing compositions, or tracking timelines, Sonatia provides a user-friendly and powerful solution to elevate your creative workflow.

---

## Features ✨
- Manage and organize multiple music projects in one place.
- Track project timelines and milestones.
- Build your music files into cohesive project folders.
- Simple, sleek, and intuitive user interface.

---

## Prerequisites 🛠️
Before running or building the project, ensure that the following are installed:
- **Python** (version 3.9 or later recommended)
- **pip** (Python's package manager)

---

## Installation 🔧
Follow these steps to set up the project:

1. **Clone the Repository**
2. **Install Dependencies**: Use the requirements.txt file to install the required Python packages.
   ```
   pip install -r requirements.txt
   ```
3. **Run the Application**: Execute the following command to start the application.
   ```
   python src/app.py
   ```

---

## Building Sonatia as a Single Executable 🏗️
To build the Sonatia application into a single executable file, you can use **PyInstaller**.

1. **Install PyInstaller**:
   ```
   pip install pyinstaller
   ```
2. **Create the Executable**: Run the following command to bundle the project into a onefile executable.
   ```
   pyinstaller --onefile src/app.py
   ```
3. **Locate the Executable**: The executable will be found in the `dist/` folder. You can rename and move it to your preferred location.

---

## License 📄

This project is licensed under the [MIT License](https://opensource.org/license/MIT).