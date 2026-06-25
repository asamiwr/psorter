# This is a simple file sorter for linux
# this app will organize files in a directory
# it will moves the videos in videos folder
# and moves pictures to pictures folder in user's home directory
# Writed with love

import shutil
from datetime import datetime
from pathlib import Path

def sorting():
    formats = {
        "video": [
            ".mp4",
            ".avi",
            ".mov",
            ".mkv",
            ".wmv",
            ".flv",
            ".webm",
            ".m4v",
            ".mpeg",
            ".mpg",
        ],
        "picture": [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".webp",
            ".svg",
            ".tiff",
            ".tif",
            ".heic",
        ],
        "document": [
            ".pdf",
            ".doc",
            ".docx",
            ".txt",
            ".rtf",
            ".odt",
            ".xlsx",
            ".xls",
            ".ppt",
            ".pptx",
            ".csv",
        ],
        "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".opus", ".m4a", ".wma"],
        "compressed": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".tgz"],
        "executables": [
            ".exe",
            ".msi",
            ".bat",
            ".cmd",
            ".com",
            ".appimage",
            ".run",
            ".bin",
            ".elf",
        ],
        "packages": [
            ".deb",
            ".rpm",
            ".pkg",
            ".apk",
            ".flatpak",
            ".flatpakref",
            ".snap",
            ".pkg.tar.zst",
            ".pkg.tar.xz",
        ],
        "disk_images": [
            ".iso",
            ".img",
            ".qcow2",
            ".vdi",
            ".vmdk",
            ".vhd",
            ".vhdx",
            ".ova",
            ".ovf",
        ],
        "code": [
            ".py",
            ".rs",
            ".c",
            ".h",
            ".cpp",
            ".hpp",
            ".java",
            ".kt",
            ".js",
            ".ts",
            ".jsx",
            ".tsx",
            ".php",
            ".go",
            ".rb",
            ".swift",
            ".dart",
            ".lua",
            ".sh",
            ".fish",
            ".zsh",
        ],
        "web": [".html", ".htm", ".css", ".js", ".ts", ".jsx", ".tsx", ".json", ".xml"],
        "config": [".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf", ".env"],
        "database": [".db", ".sqlite", ".sqlite3", ".mdb", ".accdb", ".sql"],
        "fonts": [".ttf", ".otf", ".woff", ".woff2"],
        "ebooks": [".epub", ".mobi", ".azw", ".azw3", ".fb2"],
        "3d": [".blend", ".obj", ".fbx", ".stl", ".dae", ".3ds", ".gltf", ".glb"],
        "design": [".psd", ".xcf", ".ai", ".indd", ".sketch"],
        "torrent": [".torrent"],
        "subtitles": [".srt", ".ass", ".ssa", ".sub", ".vtt"],
    }
    downloads_folder = Path.home() / "Downloads"
    for items in downloads_folder.iterdir():
        if not items.is_file():
            continue

        if items.suffix.lower() in formats["video"]:
            shutil.move(items, Path.home() / "Videos")

        elif items.suffix.lower() in formats["picture"]:
            shutil.move(items, Path.home() / "Pictures")

        elif items.suffix.lower() in formats["document"]:
            shutil.move(items, Path.home() / "Documents")

        elif items.suffix.lower() in formats["audio"]:
            shutil.move(items, Path.home() / "Music")

        elif items.suffix.lower() in formats["compressed"]:
            shutil.move(items, Path.home() / "Compressed")

        elif items.suffix.lower() in formats["executables"]:
            shutil.move(items, Path.home() / "Executables")

        elif items.suffix.lower() in formats["packages"]:
            shutil.move(items, Path.home() / "Packages")

        elif items.suffix.lower() in formats["disk_images"]:
            shutil.move(items, Path.home() / "Disk Images")

        elif items.suffix.lower() in formats["code"]:
            shutil.move(items, Path.home() / "Code")

        elif items.suffix.lower() in formats["web"]:
            shutil.move(items, Path.home() / "Web")

        elif items.suffix.lower() in formats["config"]:
            shutil.move(items, Path.home() / "Config")

        elif items.suffix.lower() in formats["database"]:
            shutil.move(items, Path.home() / "Database")

        elif items.suffix.lower() in formats["fonts"]:
            shutil.move(items, Path.home() / "Fonts")

        elif items.suffix.lower() in formats["ebooks"]:
            shutil.move(items, Path.home() / "Ebooks")

        elif items.suffix.lower() in formats["3d"]:
            shutil.move(items, Path.home() / "3D")

        elif items.suffix.lower() in formats["design"]:
            shutil.move(items, Path.home() / "Design")

        elif items.suffix.lower() in formats["torrent"]:
            shutil.move(items, Path.home() / "Torrent")

        elif items.suffix.lower() in formats["subtitles"]:
            shutil.move(items, Path.home() / "Subtitles")

        else:
            shutil.move(items, Path.home() / "Others")



def start_sorting():
    if (
        Path.home() / "Music"
        and (Path.home() / "Documents").exists()
        and (Path.home() / "Downloads").exists()
        and (Path.home() / "Pictures").exists()
        and (Path.home() / "Videos").exists()
        and (Path.home() / "Compressed").exists()
        and (Path.home() / "Executables").exists()
        and (Path.home() / "Packages").exists()
        and (Path.home() / "Disk Images").exists()
        and (Path.home() / "Code").exists()
        and (Path.home() / "Web").exists()
        and (Path.home() / "Config").exists()
        and (Path.home() / "Database").exists()
        and (Path.home() / "Fonts").exists()
        and (Path.home() / "Ebooks").exists()
        and (Path.home() / "3D").exists()
        and (Path.home() / "Design").exists()
        and (Path.home() / "Torrent").exists()
        and (Path.home() / "Subtitles").exists()
        and (Path.home() / "Others").exists()
    ):
        sorting()
    else:
        # create missing folders
        Path.mkdir(Path.home() / "Music", exist_ok=True)
        (Path.home() / "Documents").mkdir(exist_ok=True)
        (Path.home() / "Downloads").mkdir(exist_ok=True)
        (Path.home() / "Pictures").mkdir(exist_ok=True)
        (Path.home() / "Videos").mkdir(exist_ok=True)
        (Path.home() / "Compressed").mkdir(exist_ok=True)
        (Path.home() / "Executables").mkdir(exist_ok=True)
        (Path.home() / "Packages").mkdir(exist_ok=True)
        (Path.home() / "Disk Images").mkdir(exist_ok=True)
        (Path.home() / "Code").mkdir(exist_ok=True)
        (Path.home() / "Web").mkdir(exist_ok=True)
        (Path.home() / "Config").mkdir(exist_ok=True)
        (Path.home() / "Database").mkdir(exist_ok=True)
        (Path.home() / "Fonts").mkdir(exist_ok=True)
        (Path.home() / "Ebooks").mkdir(exist_ok=True)
        (Path.home() / "3D").mkdir(exist_ok=True)
        (Path.home() / "Design").mkdir(exist_ok=True)
        (Path.home() / "Torrent").mkdir(exist_ok=True)
        (Path.home() / "Subtitles").mkdir(exist_ok=True)
        (Path.home() / "Others").mkdir(exist_ok=True)
        sorting()
