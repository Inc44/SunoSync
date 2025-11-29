# SunoSync 🎵

**Download your entire Suno AI music library in seconds — with lyrics, album art, prompts, tags, and perfect metadata!**

[![Download EXE](https://img.shields.io/badge/Download-EXE-brightgreen)](https://justinmurray99.gumroad.com/l/rrxty)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

![SunoSync Screenshot](https://github.com/user-attachments/assets/15590529-18cb-4be3-9e49-ef8422aab5d0)

## ✨ Features

- ⚡ **Lightning-fast concurrent downloads** - Downloads 10-30 songs simultaneously
- 🎯 **Smart resume** - Never downloads the same song twice (tracks by UUID)
- 🎨 **Full metadata embedding** - Title, artist, genre, year, lyrics, album art, and more
- 🎵 **WAV support** - Optional high-fidelity WAV downloads when available
- 📁 **Organize by month** - Automatically sorts downloads into YYYY-MM folders
- ⏱️ **Rate limiting** - Configurable delay between downloads to avoid API limits
- 🔄 **Automatic retries** - Handles network errors gracefully
- 💾 **Persistent settings** - Your token and preferences are saved automatically
- 🎨 **Modern UI** - Beautiful dark-themed interface with real-time progress tracking

## 🚀 Quick Start

### Option 1: Download Pre-built EXE (Recommended)

**[Get the ready-to-use Windows executable →](https://justinmurray99.gumroad.com/l/rrxty)**

No installation required - just download and run!

### Option 2: Run from Source

#### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

#### Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/SunoSync.git
cd SunoSync

# 2. Create a virtual environment (recommended)
python -m venv venv

# 3. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
python suno_api_gui.py
```

## 📖 Usage Guide

### Getting Your Suno API Token

1. Open the app and click **"Get Token (Login)"**
2. Log in to [suno.com](https://suno.com) in the browser window that opens
3. Press `F12` to open Developer Tools
4. Go to the **Console** tab
5. Copy and paste this code:
   ```javascript
   window.Clerk.session.getToken().then(t => prompt('Copy this token:', t))
   ```
6. Copy the token from the popup
7. Paste it into the app

### Downloading Your Library

1. **Set your download folder** - Click "Browse" to choose where files should be saved
2. **Configure options**:
   - **Embed Metadata & Art**: Adds ID3 tags and album art to files (recommended)
   - **Download WAV when available**: Prefers WAV format for higher quality
   - **Organize by Month**: Creates subfolders like `2024-11`, `2025-01`, etc.
   - **Delay between downloads**: Add a delay (e.g., 0.5s) to avoid rate limits
3. **Set page range** (optional):
   - **Start from Page**: Resume from a specific page
   - **Max Pages**: Limit how many pages to download (0 = all pages)
4. Click **"START DOWNLOAD"** and wait for your library to download!

### File Organization

- **MP3 files** are saved with full metadata embedded
- **WAV files** (if enabled) are saved when the API provides them
- **Lyrics** are saved as `.txt` files alongside audio files
- Files are automatically renamed if duplicates exist (e.g., `song v2.mp3`)

## 🛠️ Building from Source

If you want to build your own executable:

### Requirements

- Python 3.8+
- PyInstaller: `pip install pyinstaller`

### Build Steps

```bash
# 1. Install dependencies
pip install -r requirements.txt
pip install pyinstaller

# 2. Build the executable
pyinstaller SunoApi.spec --clean

# 3. Find your executable in dist/SunoApiDownloader.exe
```

## 📁 Project Structure

```
SunoSync/
├── suno_api_gui.py      # Main GUI application
├── suno_downloader.py    # Download logic and API interaction
├── suno_utils.py         # Utility functions (metadata, file handling)
├── suno_widgets.py       # Custom Tkinter widgets
├── suno_layout.py        # Layout builders and dialogs
├── SunoApi.spec          # PyInstaller build configuration
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## ⚙️ Configuration

Settings are automatically saved to `config.json` in the application directory:

- **Token**: Your Suno API bearer token
- **Download Path**: Where files are saved
- **Embed Metadata**: Whether to add ID3 tags
- **Prefer WAV**: Whether to download WAV when available
- **Organize by Month**: Whether to create monthly subfolders
- **Download Delay**: Rate limiting delay in seconds
- **Max Pages**: Maximum pages to download (0 = all)
- **Start Page**: Which page to start from
- **Log Font Size**: Activity log text size

## 🔒 Privacy & Security

- Your API token is stored locally in `config.json` (never shared)
- All downloads happen directly between your computer and Suno's servers
- No data is sent to third parties
- The app only accesses your own Suno library

## ⚠️ Legal & Responsible Use

**Important Guidelines:**

- ✅ Only download songs **you personally generated** on Suno
- ✅ Keep your auth token **private** - never share it
- ❌ **Never re-upload** or share downloaded files publicly
- ❌ **Don't use** for bulk downloading other users' content
- ⚠️ The developer is **not responsible** for account bans resulting from misuse

Respect Suno's Terms of Service and use this tool responsibly.

## 🐛 Troubleshooting

### "Token missing" error
- Make sure you've pasted your token correctly
- Get a fresh token if it's expired

### Downloads failing
- Check your internet connection
- Try increasing the "Delay between downloads" setting
- Some songs may not be available if they were deleted

### WAV files not downloading
- WAV conversion can take up to 2 minutes per song
- The app will automatically fall back to MP3 if WAV times out
- Make sure "Download WAV when available" is enabled

### App won't start
- Make sure you have Python 3.8+ installed
- Try reinstalling dependencies: `pip install -r requirements.txt --force-reinstall`
- Check that all required files are present

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Support

- **Buy the EXE**: [Get the pre-built Windows executable](https://justinmurray99.gumroad.com/l/rrxty)
- **Report Issues**: Open an issue on GitHub
- **Feature Requests**: Submit a feature request issue

## ⭐ Acknowledgments

- Built with ❤️ for the Suno AI community
- Uses [mutagen](https://github.com/quodlibet/mutagen) for metadata embedding
- Modern UI built with Tkinter and custom widgets

---

**Made with ❤️ for the Suno AI community — 2024**
