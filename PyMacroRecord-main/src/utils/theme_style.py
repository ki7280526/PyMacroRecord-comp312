class ThemeStyle: #styles for light/dark mode (taken from color-hex.com) 
    THEMES = {
      "Light": {
      "bg": "#fafafa",
      "fg": "#1e1e1e",
      "button_bg": "#e6e6e6",
      "button_fg": "#1e1e1e"
      },
      "Dark": {
        "bg": "#1e1e1e",
        "fg": "#f2f2f2", 
        "button_bg": "#2d2d2d",
        "button_fg": "#f2f2f2"
      }
  }

def get(theme_option: str): 
  return ThemeStyle.THEMES.get(theme_option, ThemeStyle.THEMES["Light"])
