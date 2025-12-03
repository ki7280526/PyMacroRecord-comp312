from sys import platform

from windows import MainApp

if platform.lower() == "win32":
    import ctypes
    PROCESS_PER_MONITOR_DPI_AWARE = 2
    ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)
def mac_permissions(): 
    if platform.lower() == "darwin":
        print(
            """
macOS - Keyboard recording may require permissions. 
If you see 'AXIsProcessTrusted' errors, follow these steps: 
1. Run: which python3 (copy path)
2. Open: 
   System Settings -> Privacy & Security -> Accessibility
3. Click the + button, then press Command + Shift + G and paste path.
4. Add Terminal too.
5. Ensure both are toggled ON, restart Terminal.
"""
        )
mac_permissions()
            

if __name__ == "__main__":
    MainApp()
