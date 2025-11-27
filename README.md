SunoSync – Source Code Repository 🎵
Download your entire Suno AI music library with full metadata, lyrics, album art, and perfect ID3 tags
⚠️ This is the official open-source repository for SunoSync (v2.4.0+).
The tool remains unofficial and not affiliated with Suno AI. Use only for personal backup of songs you created.
Features

Super-fast concurrent downloads (10–30 songs at once)
Full embedded metadata & album art (title, artist, genre, year, lyrics, original prompt, tags)
Smart resume / duplicate-safe resume
Optional monthly folder organization
Real-time progress bar, speed, and ETA
Automatic retry on network errors
Persistent settings & token storage

Installation & Running from Source
Bash# 1. Clone the repository
git clone https://github.com/yourusername/SunoSync.git
cd SunoSync

# 2. (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the GUI
python suno_api_gui.py
How to Build the Executable (Windows .exe) – for contributors
Bash# Make sure you're in the activated virtual environment with all deps installed

# One-file bundled executable (recommended for distribution)
pyinstaller --onefile --windowed --icon=icon.ico --name="SunoSync" suno_api_gui.py

# Or with separate files + faster startup (smaller updates)
# pyinstaller --onedir --windowed --icon=icon.ico --name="SunoSync" suno_api_gui.py

# The executable will be in ./dist/
Extra PyInstaller tips used in the official build:
Bash--add-data "icon.ico;."              # include the app icon
--add-data "README.md;."             # optional
--hidden-import=plyer.platforms.win.notification  # fixes missing tray icon on some systems
Project Structure
textSunoSync/  
├── suno_api_gui.py          # Main application (PyQt6)  
├── downloader.py            # Core downloading logic  
├── utils.py                 # Metadata embedding, ID3, etc.  
├── icon.ico                 # App icon  
├── requirements.txt  
├── LICENSE                  # MIT License  
└── .gitignore  

## License
This project is licensed under the MIT License – see the LICENSE file for details.

## Legal Notice & Responsible Use
- Only use this software to back up music you personally generated on Suno.com  
- Do not redistribute downloaded songs (this violates Suno’s ToS and risks account termination)  
- The developer is not responsible for any account bans or consequences of misuse  

Made with ❤️ for the Suno AI community  
If you appreciate this tool, consider supporting it: https://buymeacoffee.com/audioalchemy

---

### Recommended files to create right now:

**`requirements.txt`**
```txt
PyQt6>=6.7.0
requests>=2.31.0
tqdm>=4.66.0
mutagen>=1.47.0
Pillow>=10.0.0
plyer>=2.1.0
pyinstaller>=6.0.0
LICENSE (MIT)
textMIT License

Copyright (c) 2025 Your Name / AudioAlchemy

Permission is hereby granted, free of charge, to any person obtaining a copy...
(standard MIT text)
.gitignore
gitignore__pycache__/
*.pyc
venv/
build/
dist/
*.spec
*.token
config.json
SunoSync.exe
Now you’re ready to push the repo to GitHub with full transparency and easy contribution/build instructions! Let me know if you want a dark mode version of the README with badges, screenshots, or GitHub Actions for auto-builds, etc. 🚀
