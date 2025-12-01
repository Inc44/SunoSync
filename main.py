import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import json
import sys
from library_tab import LibraryTab
from player_widget import PlayerWidget
from downloader_tab import DownloaderTab
from config_manager import ConfigManager

if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(base_path, "config.json")
CACHE_FILE = os.path.join(base_path, "library_cache.json")
TAGS_FILE = os.path.join(base_path, "tags.json")


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class SunoSyncApp(tk.Tk):
    """Main application with Downloader, Library, and Player."""
    
    def __init__(self):
        super().__init__()
        
        self.withdraw()  # Hide initially for splash
        
        self.title("SunoSync")
        
        # Set Icon
        try:
            icon_path = resource_path("resources/icon.ico")
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)
        except Exception as e:
            print(f"Icon error: {e}")

        # Load geometry
        self.load_window_state()
        
        # Theme colors
        self.bg_dark = "#1a1a1a"
        self.configure(bg=self.bg_dark)
        
        # Main layout
        main_frame = tk.Frame(self, bg=self.bg_dark)
        main_frame.pack(fill="both", expand=True)
        
        # Create tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Shared Config Manager
        self.config_manager = ConfigManager(CONFIG_FILE)
        
        # Tab 1: Downloader
        self.downloader = DownloaderTab(self.notebook, config_manager=self.config_manager)
        self.notebook.add(self.downloader, text="  Downloader  ")
        
        # Tab 2: Library
        self.library = LibraryTab(self.notebook, config_manager=self.config_manager, cache_file=CACHE_FILE, tags_file=TAGS_FILE)
        self.notebook.add(self.library, text="  Library  ")
        
        # Player widget (bottom, fixed)
        self.player = PlayerWidget(main_frame)
        self.player.set_tags_file(TAGS_FILE)
        self.player.pack(fill="x", side="bottom")
        
        # Connect Library to Player
        self.library.bind("<<PlaySong>>", self.on_play_song)
        self.player.bind("<<TagsUpdated>>", lambda e: self.library.reload_tags())
        self.player.bind("<<TrackChanged>>", self.on_track_changed)
        
        # Connect Downloader to Library (refresh on download complete)
        self.downloader.downloader.signals.download_complete.connect(self.on_download_complete)
        
        # Style notebook
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background=self.bg_dark, borderwidth=0)
        style.configure("TNotebook.Tab",
                       background="#2d2d2d",
                       foreground="#e0e0e0",
                       padding=[20, 10],
                       font=("Segoe UI", 10, "bold"))
        style.map("TNotebook.Tab",
                 background=[("selected", "#8b5cf6")],
                 foreground=[("selected", "white")])
                 
        # Version Label (Bottom Right of Main Window, overlay or status bar?)
        # Let's put it in the player widget or just a small label?
        # Player widget is at bottom.
        # I'll add it to the player widget in a moment, or just ignore for main window if splash has it.
        
        # Handle close
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Show Splash
        self.show_splash()
    
    def show_splash(self):
        """Show splash screen."""
        splash_path = resource_path("resources/splash.png")
        if not os.path.exists(splash_path):
            self.deiconify()
            return
            
        splash = tk.Toplevel(self)
        splash.overrideredirect(True)
        
        try:
            pil_img = Image.open(splash_path)
            # Resize to reasonable size
            pil_img.thumbnail((600, 400))
            img = ImageTk.PhotoImage(pil_img)
            
            lbl = tk.Label(splash, image=img, bg="black")
            lbl.image = img
            lbl.pack()
            
            # Center splash
            w = pil_img.width
            h = pil_img.height
            ws = self.winfo_screenwidth()
            hs = self.winfo_screenheight()
            x = int((ws/2) - (w/2))
            y = int((hs/2) - (h/2))
            splash.geometry(f'{w}x{h}+{x}+{y}')
            
            # Version
            tk.Label(splash, text="v2.0", bg="black", fg="white", 
                    font=("Segoe UI", 12, "bold")).place(relx=0.95, rely=0.95, anchor="se")
            
        except Exception as e:
            print(f"Splash error: {e}")
            splash.destroy()
            self.deiconify()
            return

        def end_splash():
            splash.destroy()
            self.deiconify()
            self.check_changelog()
            
        self.after(2000, end_splash)

    def check_changelog(self):
        """Show changelog on first launch of new version."""
        current_version = "2.0"
        last_version = None
        state_file = "window_state.json"
        data = {}
        
        if os.path.exists(state_file):
            try:
                with open(state_file, "r") as f:
                    data = json.load(f)
                    last_version = data.get("version")
            except:
                pass
        
        if last_version != current_version:
            # Show Changelog
            messagebox.showinfo("What's New in v2.0", 
                "🎉 Welcome to SunoSync v2.0! 🎉\n\n"
                "• New Modular Interface: Downloader, Library, and Player in one app.\n"
                "• Built-in Audio Player: Play your songs directly.\n"
                "• Library Management: Search, sort, and manage your downloads.\n"
                "• Lyrics Editor: View and edit embedded lyrics.\n"
                "• Improved Stability & Performance.\n\n"
                "Enjoy your music!")
            
            # Save new version
            data["version"] = current_version
            try:
                with open(state_file, "w") as f:
                    json.dump(data, f)
            except:
                pass

    def load_window_state(self):
        try:
            if os.path.exists("window_state.json"):
                with open("window_state.json", "r") as f:
                    data = json.load(f)
                    self.geometry(data.get("geometry", "1100x750"))
            else:
                self.geometry("1100x750")
        except:
            self.geometry("1100x750")

    def on_close(self):
        try:
            with open("window_state.json", "w") as f:
                json.dump({"geometry": self.geometry()}, f)
        except:
            pass
        self.destroy()

    def on_download_complete(self, success):
        """Refresh library when downloads complete."""
        if success:
            self.library.refresh_library()
    
    def on_play_song(self, event):
        """Handle play song event from library."""
        # Get playlist and index from library
        if hasattr(self.library, 'current_playlist') and hasattr(self.library, 'current_index'):
            self.player.set_playlist(self.library.current_playlist, self.library.current_index)

    def on_track_changed(self, event):
        """Handle track change from player."""
        if self.player.current_file:
            self.library.select_song(self.player.current_file)


if __name__ == "__main__":
    app = SunoSyncApp()
    app.mainloop()
