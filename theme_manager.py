from PIL import ImageFont

class ThemeManager:
    def __init__(self):
        # Modern Dark Mode Palette
        self.bg_dark = "#121212"      # Main background
        self.card_bg = "#1E1E1E"      # Card/Panel background
        self.bg_card = self.card_bg   # Alias
        self.bg_input = "#2C2C2C"     # Input fields
        self.fg_primary = "#E0E0E0"   # Main text
        self.fg_secondary = "#A0A0A0" # Secondary text
        
        self.accent_purple = "#8B5CF6" # Primary Action (Matte Purple)
        self.accent_pink = "#EC4899"   # Secondary Accent
        self.accent_red = "#EF4444"    # Destructive Action
        
        self.border_subtle = "#333333" # Subtle borders
        self.card_border = "#333333"   # Card borders
        
        self.section_font = ("Segoe UI", 11, "bold")
        self.title_font = ("Segoe UI", 24, "bold")
        self.mono_font = ("Consolas", 10)

    def load_title_font(self, size):
        # Fallback to Segoe UI for title as well, keeping it clean
        return ImageFont.truetype("arial.ttf", size) 

