class ThemeStyle: #styles for light/dark mode (taken from color-hex.com & figman.com) 
    THEMES = {
      "Light": {
      "bg": "#fafafa",
      "fg": "#1e1e1e",
      "status_bg": "#e0e0e0",
      "status_fg": "#1e1e1e"
      },
      "Dark": {
        "bg": "#1e1e1e",
        "fg": "#f2f2f2", 
        "status_bg": "#2a2a2a",
        "status_fg": "#f2f2f2"
      },
      "Neon Noir": {
        "bg": "#030056",
        "fg": "#8ffcff", 
        "status_bg": "#000000",
        "status_fg": "#8ffcff"
      },
      "Space Berries": {
        "bg": "#ffb8dc",
        "fg": "#8c1946", 
        "status_bg": "#8c1946",
        "status_fg": "#ffb8dc"
      },
      "Jolly": {
        "bg": "#8e0a1e",
        "fg": "#add8e6", 
        "status_bg": "#2e6f40",
        "status_fg": "#ffffff"
      },
      "Coffee": {
        "bg": "#967259",
        "fg": "#dbc1ac", 
        "status_bg": "#634832",
        "status_fg": "#dbc1ac"
      },
      "Forest": {
        "bg": "#243b2c",
        "fg": "#a8c391", 
        "status_bg": "#627c5c",
        "status_fg": "#a8c391"
      }
  }

def get(theme_option: str): 
  return ThemeStyle.THEMES.get(theme_option, ThemeStyle.THEMES["Light"])
