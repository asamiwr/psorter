# 📂 PSorter

A simple and lightweight file organizer for Linux written in Python.

PSorter automatically sorts files from your `Downloads` directory into categorized folders inside your home directory, either immediately or at a scheduled time.

## ✨ Features

* Organizes files by extension
* Creates missing folders automatically
* Supports many common file formats
* Schedule sorting for a specific time
* Uses only Python's standard library
* No external dependencies

## 📦 Installation

```bash
git clone https://github.com/asamiwr/psorter.git
cd psorter
```

## 🚀 Usage

Sort files immediately:

```bash
python3 main.py
```

Schedule sorting:

```bash
python3 main.py 02:12
```

Time must be provided in **24-hour format (HH:MM)**.

Examples:

```bash
python3 main.py 02:12
python3 main.py 18:30
python3 main.py 23:59
```

If the specified time has already passed today, PSorter will automatically wait until the next day.

## ⚠️ Warning

PSorter moves files from your Downloads directory into categorized folders. Test it with sample files before using it on important data.

## 🛠 Requirements

* Linux
* Python 3.10+

## 🤝 Contributing

Issues, suggestions, and pull requests are welcome.

## 📄 License

MIT License

## ❤️ Author

Created by AmirHossein.
