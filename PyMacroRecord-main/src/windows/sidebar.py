import tkinter as tk
from tkinter import ttk


class Sidebar(tk.Frame):
    """
    Collapsible sidebar for PyMacroRecord.

    controller is expected to be MainApp and provide:
      - start_record, stop_record, start_playback
      - open_macro, save_macro
      - open_repetitions, open_speed_interval, open_interval, open_for_loop
      - open_schedule, open_after_playback
      - open_hotkeys, open_settings
      - show_status_window, show_about_window   (optional)
    """

    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.controller = controller
        self.expanded_width = 220
        self.collapsed_width = 48
        self.is_collapsed = False

        self.config(bg="#20232a", width=self.expanded_width)
        self.grid_propagate(False)

        # Top bar: toggle + title
        top = tk.Frame(self, bg="#20232a")
        top.grid(row=0, column=0, sticky="ew")
        top.columnconfigure(1, weight=1)

        self.toggle_btn = tk.Button(
            top,
            text="⮜",  # arrow left when expanded
            command=self.toggle,
            bg="#20232a",
            fg="#ffffff",
            relief="flat",
            activebackground="#2c313c",
            activeforeground="#ffffff",
            bd=0,
            padx=4,
            pady=2,
            font=("Segoe UI", 10, "bold"),
        )
        self.toggle_btn.grid(row=0, column=0, sticky="w", padx=4, pady=4)

        self.title_lbl = tk.Label(
            top,
            text="PyMacroRecord",
            bg="#20232a",
            fg="#ffffff",
            font=("Segoe UI", 11, "bold"),
        )
        self.title_lbl.grid(row=0, column=1, sticky="w", padx=4, pady=4)

        # Content area that holds sections
        self.content = tk.Frame(self, bg="#20232a")
        self.content.grid(row=1, column=0, sticky="nsew")
        self.rowconfigure(1, weight=1)

        # Build all sections
        self._build_main_controls()
        self._build_macro_controls()
        self._build_playback_options()
        self._build_after_playback()
        self._build_hotkeys_settings()
        self._build_info_section()

    # --------- UI building helpers ---------

    def _build_main_controls(self):
        section = self._make_section(self.content, "Main")
        self._make_button(section, "● Record", self.controller.start_record)
        self._make_button(section, "■ Stop", self.controller.stop_record)
        self._make_button(section, "▶ Play", self.controller.start_playback)

    def _build_macro_controls(self):
        section = self._make_section(self.content, "Macro")
        self._make_button(section, "Open macro…", self.controller.open_macro)
        self._make_button(section, "Save macro…", self.controller.save_macro)

    def _build_playback_options(self):
        # Options that match core features: repetitions, speed, interval, for, schedule [web:18][web:2]
        section = self._make_section(self.content, "Playback")
        self._make_button(section, "Repetitions / Loop", self.controller.open_repetitions)
        self._make_button(section, "Speed", self.controller.open_speed_interval)
        self._make_button(section, "Interval", self.controller.open_interval)
        self._make_button(section, "For (duration)", self.controller.open_for_loop)
        self._make_button(section, "Schedule", self.controller.open_schedule)

    def _build_after_playback(self):
        section = self._make_section(self.content, "After playback")
        self._make_button(section, "Actions (shutdown, etc.)", self.controller.open_after_playback)

    def _build_hotkeys_settings(self):
        section = self._make_section(self.content, "Hotkeys & Settings")
        self._make_button(section, "Hotkeys", self.controller.open_hotkeys)
        self._make_button(section, "Settings", self.controller.open_settings)

    def _build_info_section(self):
        section = self._make_section(self.content, "Info")
        self._make_button(section, "Show status", getattr(self.controller, "show_status_window", lambda: None))
        self._make_button(section, "About", getattr(self.controller, "show_about_window", lambda: None))

    def _make_section(self, master, title):
        container = tk.Frame(master, bg="#20232a")
        container.pack(fill="x", pady=(6, 2))

        title_lbl = tk.Label(
            container,
            text=title,
            bg="#20232a",
            fg="#bbbbbb",
            anchor="w",
            font=("Segoe UI", 9, "bold"),
        )
        title_lbl.pack(fill="x", padx=8)

        inner = tk.Frame(container, bg="#20232a")
        inner.pack(fill="x", padx=4)
        return inner

    def _make_button(self, master, text, command):
        btn = tk.Button(
            master,
            text=text,
            command=command,
            anchor="w",
            relief="flat",
            bg="#20232a",
            fg="#ffffff",
            activebackground="#2c313c",
            activeforeground="#ffffff",
            padx=10,
            pady=4,
            borderwidth=0,
            highlightthickness=0,
        )
        btn.pack(fill="x", pady=1)

    # --------- Collapse / expand ---------

    def toggle(self):
        """Collapse or expand the sidebar."""
        self.is_collapsed = not self.is_collapsed

        if self.is_collapsed:
            # Collapse: shrink width and hide text labels/sections
            self.config(width=self.collapsed_width)
            self.title_lbl.config(text="")
            self.content.grid_remove()
            self.toggle_btn.config(text="⮞")  # arrow right when collapsed
        else:
            # Expand: restore width and show content
            self.config(width=self.expanded_width)
            self.title_lbl.config(text="PyMacroRecord")
            self.content.grid(row=1, column=0, sticky="nsew")
            self.toggle_btn.config(text="⮜")

        self.update_idletasks()
    #function for sidebar theme application 
    def apply_theme(self, theme):
        try:
            #main bg 
            self.config(bg=theme["sidebar_bg"])
            self.content.config(bg=theme["sidebar_bg"])
            
            #Collapse/toggle 
            self.toggle_btn.config(
                bg=theme["sidebar_bg"],
                fg=theme["sidebar_fg"],
                activebackground=theme["sidebar_button_hover_bg"],
                activeforeground=theme["sidebar_button_hover_fg"],
            )

            #Title (next to collapse)
            self.title_lbl.config(
                bg=theme["sidebar_bg"],
                fg=theme["sidebar_fg"],
            )
            #applying to subwidgets using subwidgets_theme func.
            self.subwidgets_theme(self, theme)
        except Exception as e:
            print("Theme error on sidebar", e)
    #funtion for theme application on all widgets INSIDE the sidebar
    def subwidgets_theme(self, widget, theme):
        #frame 
        if isinstance(widget, tk.Frame):
            widget.config(bg=theme["sidebar_bg"])
        
        #labels 
        elif isinstance(widget, tk.Label):
            font_details= str(widget.cget("font"))
            #headers/sections
            if "bold" in font_details and "9" in font_details:
                #headers/sections modifications
                widget.config(
                    bg=theme["sidebar_bg"],
                    fg=theme["sidebar_section_fg"],              
                )
            else:
                widget.config(
                    bg=theme["sidebar_bg"],
                    fg=theme["sidebar_fg"],
                )
        #Buttoms theme application
        elif isinstance(widget, tk.Button):
            widget.config(
                bg= theme["sidebar_button_bg"],
                fg= theme["sidebar_button_fg"],
                activebackground= theme["sidebar_button_hover_bg"],
                activeforeground= theme["sidebar_button_hover_fg"], 
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
                takefocus=0
            )
        
        #loop through subwidgets 
        for subwidget in widget.winfo_children():
            self.subwidgets_theme(subwidget, theme)







