# 📂 PSorter

A simple and lightweight file organizer for Linux written in Python.

PSorter automatically sorts files from your `Downloads` directory into categorized folders inside your home directory.

Perfect for users who are tired of having hundreds of files cluttering their Downloads folder.

---

## ✨ Features

* Automatically scans your Downloads directory
* Creates missing destination folders automatically
* Sorts files by extension
* Supports many common file formats
* Uses only Python's standard library
* No external dependencies required
* Lightweight and easy to modify

---

## 📁 Supported Categories

PSorter can organize files into the following folders:

| Category            | Destination Folder |
| ------------------- | ------------------ |
| Videos              | `~/Videos`         |
| Pictures            | `~/Pictures`       |
| Documents           | `~/Documents`      |
| Music               | `~/Music`          |
| Compressed Archives | `~/Compressed`     |
| Executables         | `~/Executables`    |
| Packages            | `~/Packages`       |
| Disk Images         | `~/Disk Images`    |
| Source Code         | `~/Code`           |
| Web Files           | `~/Web`            |
| Configuration Files | `~/Config`         |
| Databases           | `~/Database`       |
| Fonts               | `~/Fonts`          |
| E-Books             | `~/Ebooks`         |
| 3D Models           | `~/3D`             |
| Design Files        | `~/Design`         |
| Torrents            | `~/Torrent`        |
| Subtitles           | `~/Subtitles`      |
| Unknown Files       | `~/Others`         |

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/psorter.git
cd psorter
```

Create a virtual environment (optional):

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

> PSorter currently uses only Python's standard library, so no external packages are required.

---

## 🚀 Usage

Run the program:

```bash
python3 main.py
```

PSorter will:

1. Create missing destination folders
2. Scan your Downloads directory
3. Detect file types
4. Move files into their appropriate folders

---

## 📖 Example

### Before

```text
Downloads/
├── movie.mp4
├── wallpaper.png
├── archive.zip
├── script.py
├── ubuntu.iso
└── song.mp3
```

### After

```text
Videos/
└── movie.mp4

Pictures/
└── wallpaper.png

Compressed/
└── archive.zip

Code/
└── script.py

Disk Images/
└── ubuntu.iso

Music/
└── song.mp3
```

---

## ⚠️ Warning

PSorter moves files permanently from the Downloads directory.

Before using it on important data:

* Test it with a few sample files
* Review the supported file extensions
* Make sure destination folders are correct

---

## 🛠 Requirements

* Linux
* Python 3.10+

Check your Python version:

```bash
python3 --version
```

---

## 🤝 Contributing

Contributions, suggestions, bug reports, and pull requests are welcome.

If you have an idea for a new file category or feature, feel free to open an issue.

---

## 📄 License

MIT License

---

## ❤️ Author

Created by AmirHossein.

Written with love for Linux users who hate messy Downloads folders.
