class ThemeStyle: #styles for light/dark mode (taken from color-hex.com & figman.com) 
    THEMES = {
        "Light": {
            "bg": "#f5f5f7",
            "fg": "#1e1e1e",
            "status_bg": "#e6e6e6",
            "status_fg": "#1e1e1e",
            #Added Keys for Jacobs sidebar
            "sidebar_bg": "#ffffff",
            "sidebar_fg": "#1e1e1e",
            "sidebar_section_fg": "#6a6a6a",
            "sidebar_button_bg": "#f0f0f0",
            "sidebar_button_fg": "#1e1e1e",
            "sidebar_button_hover_bg": "#e4e4e7",
            "sidebar_button_hover_fg": "#1e1e1e",
            "button_bg": "#f0f0f0",
            "button_fg": "#1e1e1e"
        },

        "Dark": {
            "bg": "#1e1e1e",
            "fg": "#f2f2f2", 
            "status_bg": "#2a2a2a",
            "status_fg": "#f2f2f2",
            "sidebar_bg": "#252525",
            "sidebar_fg": "#f2f2f2",
            "sidebar_section_fg": "#9a9a9a",
            "sidebar_button_bg": "#3a3a3a",
            "sidebar_button_fg": "#f2f2f2",
            "sidebar_button_hover_bg": "#4a4a4a",
            "sidebar_button_hover_fg": "#ffffff",  # slight brightness on hover
            "button_bg": "#3a3a3a",
            "button_fg": "#f2f2f2"
        },

        "Neon Noir": {
            "bg": "#030056",
            "fg": "#8ffcff", 
            "status_bg": "#000000",
            "status_fg": "#8ffcff",
            "sidebar_bg": "#020040",
            "sidebar_fg": "#8ffcff",
            "sidebar_section_fg": "#5fb3b5",
            "sidebar_button_bg": "#050570",
            "sidebar_button_fg": "#8ffcff",
            "sidebar_button_hover_bg": "#0707a0",
            "sidebar_button_hover_fg": "#ffffff",
            "button_bg": "#050570",
            "button_fg": "#8ffcff"
        },

        "Space Berries": {
            "bg": "#ffb8dc",
            "fg": "#8c1946", 
            "status_bg": "#8c1946",
            "status_fg": "#ffb8dc",
            "sidebar_bg": "#ffc0e0",
            "sidebar_fg": "#8c1946",
            "sidebar_section_fg": "#b85577",
            "sidebar_button_bg": "#f5a0c8",
            "sidebar_button_fg": "#8c1946",
            "sidebar_button_hover_bg": "#ff90c0",
            "sidebar_button_hover_fg": "#6a0f34",
            "button_bg": "#f5a0c8",
            "button_fg": "#8c1946"
        },

        "Jolly": {
            "bg": "#8e0a1e",
            "fg": "#add8e6", 
            "status_bg": "#2e6f40",
            "status_fg": "#ffffff",
            "sidebar_bg": "#a01225",
            "sidebar_fg": "#add8e6",
            "sidebar_section_fg": "#87b8c7",
            "sidebar_button_bg": "#b51530",
            "sidebar_button_fg": "#add8e6",
            "sidebar_button_hover_bg": "#d01840",
            "sidebar_button_hover_fg": "#ffffff",
            "button_bg": "#b51530",
            "button_fg": "#add8e6"
        },

        "Coffee": {
            "bg": "#967259",
            "fg": "#dbc1ac", 
            "status_bg": "#634832",
            "status_fg": "#dbc1ac",
            "sidebar_bg": "#8a6650",
            "sidebar_fg": "#dbc1ac",
            "sidebar_section_fg": "#c5a590",
            "sidebar_button_bg": "#7e5a45",
            "sidebar_button_fg": "#dbc1ac",
            "sidebar_button_hover_bg": "#a57e65",
            "sidebar_button_hover_fg": "#f0d8c5",
            "button_bg": "#7e5a45",
            "button_fg": "#dbc1ac"
        },
        
        "Forest": {
            "bg": "#243b2c",
            "fg": "#a8c391", 
            "status_bg": "#627c5c",
            "status_fg": "#a8c391",
            "sidebar_bg": "#1e3125",
            "sidebar_fg": "#a8c391",
            "sidebar_section_fg": "#8fa77b",
            "sidebar_button_bg": "#304a38",
            "sidebar_button_fg": "#a8c391",
            "sidebar_button_hover_bg": "#3d5945",
            "sidebar_button_hover_fg": "#c0d8b0",
            "button_bg": "#304a38",
            "button_fg": "#a8c391"
        }
    }

def get(theme_option: str): 
    return ThemeStyle.THEMES.get(theme_option, ThemeStyle.THEMES["Light"])
