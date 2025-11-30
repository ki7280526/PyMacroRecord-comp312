import copy
import json
import sys
from json import load
from os import path
from sys import platform, argv
from threading import Thread
from time import time
from tkinter import *

from PIL import Image
from pystray import Icon
from pystray import MenuItem

from hotkeys.hotkeys_manager import HotkeysManager
from macro import Macro
from utils.get_file import resource_path
from utils.not_windows import NotWindows
from utils.record_file_management import RecordFileManagement
from utils.user_settings import UserSettings
from utils.version import Version
from utils.warning_pop_up_save import confirm_save
from windows.main.menu_bar import MenuBar
from windows.others.new_ver_avalaible import NewVerAvailable
from windows.window import Window
from windows.sidebar import Sidebar 

if platform.lower() == "win32":
    from tkinter.ttk import *

def deepcopy_dict_missing_entries(dst:dict,src:dict):
# recursively copy entries that are in src but not in dst
    for k,v in src.items():
        if k not in dst:
            dst[k] = copy.deepcopy(v)
        elif isinstance(v,dict):
            deepcopy_dict_missing_entries(dst[k],v)

class MainApp(Window):
    """Main windows of the application"""

    def __init__(self):
        super().__init__("PyMacroRecord", 350, 200)
        self.attributes("-topmost", 1)
        if platform == "win32":
            pass
            #self.iconbitmap(resource_path(path.join("assets", "logo.ico")))

        self.settings = UserSettings(self)

        self.load_language()

        # For save message purpose
        self.macro_saved = False
        self.macro_recorded = False
        self.current_file = None
        self.prevent_record = False

        self.version = Version(self.settings.settings_dict, self)

        self.menu = MenuBar(self)  # Menu Bar
        self.macro = Macro(self)

        self.validate_cmd = self.register(self.validate_input)

        self.hotkeyManager = HotkeysManager(self)

        self.status_text = Label(self, text='', relief=SUNKEN, anchor=W)
        if self.settings.settings_dict["Recordings"]["Show_Events_On_Status_Bar"]:
            self.status_text.pack(side=BOTTOM, fill=X)

        

        # Main Buttons (Start record, stop record, start playback, stop playback)

        # Play Button
        self.playImg = PhotoImage(file=resource_path(path.join("assets", "button", "play.png")))

        self.center_frame = Frame(self)
        self.center_frame.pack(expand=True, fill=BOTH)

        # Import record if opened with .pmr extension
        if len(argv) > 1:
            with open(sys.argv[1], 'r') as record:
                loaded_content = load(record)
            self.macro.import_record(loaded_content)
            self.playBtn = Button(self.center_frame, image=self.playImg, command=self.macro.start_playback)
            self.macro_recorded = True
            self.macro_saved = True
        else:
            self.playBtn = Button(self.center_frame, image=self.playImg, state=DISABLED)
        self.playBtn.pack(side=LEFT, padx=50)

        # Record Button
        self.recordImg = PhotoImage(file=resource_path(path.join("assets", "button", "record.png")))
        self.recordBtn = Button(self.center_frame, image=self.recordImg, command=self.macro.start_record)
        self.recordBtn.pack(side=RIGHT, padx=50)

        # Stop Button
        self.stopImg = PhotoImage(file=resource_path(path.join("assets", "button", "stop.png")))

        record_management = RecordFileManagement(self, self.menu)

        self.bind('<Control-Shift-S>', record_management.save_macro_as)
        self.bind('<Control-s>', record_management.save_macro)
        self.bind('<Control-l>', record_management.load_macro)
        self.bind('<Control-n>', record_management.new_macro)

        self.protocol("WM_DELETE_WINDOW", self.quit_software)
        if platform.lower() != "darwin":
            Thread(target=self.systemTray).start()

        self.attributes("-topmost", 0)

        if platform != "win32" and self.settings.first_time:
            NotWindows(self)

        if self.settings.settings_dict["Others"]["Check_update"]:
            if self.version.new_version != "" and self.version.version != self.version.new_version:
                if time() > self.settings.settings_dict["Others"]["Remind_new_ver_at"]:
                    NewVerAvailable(self, self.version.new_version)
        self.mainloop()

    def start_record(self):
        """Start recording (sidebar action)."""
        if not self.prevent_record:
            self.macro.start_record()

    def stop_record(self):
        """Stop recording or playback (sidebar action)."""
        # Adjust to your Macro implementation
        if hasattr(self.macro, "stop_record"):
            self.macro.stop_record()
        elif hasattr(self.macro, "stop"):
            self.macro.stop()

    def start_playback(self):
        """Start playback (sidebar action)."""
        self.macro.start_playback()

    def open_macro(self):
        """Open macro from file (sidebar action)."""
        RecordFileManagement(self, self.menu).load_macro()

    def save_macro(self):
        """Save macro to file (sidebar action)."""
        RecordFileManagement(self, self.menu).save_macro()

    # ---- Playback options that reflect documented features ----
    # Repetitions, speed, interval, for, schedule, after-playback [web:18][web:2]

    def open_repetitions(self):
        """Open repetitions/loop options (sidebar action)."""
        # Call into your group’s repetitions UI if you have one
        if hasattr(self.macro, "open_repetitions_window"):
            self.macro.open_repetitions_window()

    def open_speed_interval(self):
        """Open speed options (sidebar action)."""
        # If you have a dedicated speed dialog, call it here
        if hasattr(self.macro, "open_speed_window"):
            self.macro.open_speed_window()

    def open_interval(self):
        """Open interval playback options (sidebar action)."""
        if hasattr(self.macro, "open_interval_window"):
            self.macro.open_interval_window()

    def open_for_loop(self):
        """Open 'For' (duration-based loop) options (sidebar action)."""
        if hasattr(self.macro, "open_for_window"):
            self.macro.open_for_window()

    def open_schedule(self):
        """Open scheduling options (sidebar action)."""
        if hasattr(self.macro, "open_schedule_window"):
            self.macro.open_schedule_window()

    def open_after_playback(self):
        """Open after-playback actions window (sidebar action)."""
        if hasattr(self.macro, "open_after_playback_window"):
            self.macro.open_after_playback_window()

    # ---- Hotkeys & settings ----

    def open_hotkeys(self):
        """Open hotkeys configuration (sidebar action)."""
        # If your group added a specific hotkeys window, call that here;
        # otherwise, fall back to whatever opens hotkeys in the menu.
        if hasattr(self.hotkeyManager, "open_hotkeys_window"):
            self.hotkeyManager.open_hotkeys_window()

    def open_settings(self):
        """Open general settings (sidebar action)."""
        # Depending on your implementation, this might be in UserSettings or another window
        if hasattr(self.settings, "open_settings_window"):
            self.settings.open_settings_window()

    # ---- Optional Info section hooks ----

    def show_status_window(self):
        """Example hook for 'Show status' button."""
        # Implement or connect to any existing status/log window
        pass

    def show_about_window(self):
        """Example hook for 'About' button."""
        # If you already have an About window, call it here instead of pass
        if hasattr(self, "about_window"):
            try:
                self.about_window.lift()
            except Exception:
                pass


    def load_language(self):
        self.lang = self.settings.settings_dict["Language"]
        with open(resource_path(path.join('langs', self.lang + '.json')), encoding='utf-8') as f:
            self.text_content = json.load(f)
        self.text_content = self.text_content["content"]

        if self.lang != "en":
            with open(resource_path(path.join('langs', 'en.json')), encoding='utf-8') as f:
                en = json.load(f)
            deepcopy_dict_missing_entries(self.text_content, en["content"])

    def systemTray(self):
        """Just to show little icon on system tray"""
        image = Image.open(resource_path(path.join("assets", "logo.ico")))
        menu = (
            MenuItem('Show', action=self.deiconify, default=True),
        )
        self.icon = Icon("name", image, "PyMacroRecord", menu)
        self.icon.run()

    def validate_input(self, action, value_if_allowed):
        """Prevents from adding letters on an Entry label"""
        if action == "1":  # Insert
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        return True

    def quit_software(self, force=False):
        if not self.macro_saved and self.macro_recorded and not force:
            wantToSave = confirm_save(self)
            if wantToSave:
                RecordFileManagement(self, self.menu).save_macro()
            elif wantToSave == None:
                return
        if platform.lower() != "darwin":
            self.icon.stop()
        if platform.lower() == "linux":
            self.destroy()
        self.quit()
