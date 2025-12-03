# PyMacroRecord comp312

**Team 7 Project** by Zahidul Jhonny, Jacob Waag, and Jennifer Nambo
## Our Goal/Mission Statement

We wished to have more hands on experince working as a group to work on open source projects.  Which will give us an edge for any future prospects if we have in the future.
To do so we worked on PyMacroRecord an open source project that makes Macros for automation for free.  Which will let us work on a project that's useful for everday life and something we can use in th future.
While also being something that can hone our skills.

## Features Implemented
- **Enhanced Status Bar**: Extended to display repeat count and elapsed time during macro playback
- **UI Improvements**: Added light/dark mode option
- **Python Script Export**: Export macros as executable Python scripts for cross-machine compatibility and code transparency
- **Python Script Export test code**: If the exporting feature doesn't work we added test_export.py test_import.py to make python files from the regular JSON files.
- **Hindi Translation**: Added `hi.json` for Hindi language support (हिंदी भाषा समर्थन) and overall expansion on supported languges
- **MacOS Warning**: Added to help with MacOS accessibility permission instructions
- **Resizeable window**: You can change the window to any size you want, like changing sizes for a chrome tab for example.

## Technical Journey
Starting from brainstorming various AI-heavy projects, we ultimately selected PyMacroRecord for its practical utility and approachable codebase. The process of implementing our features, particularly the Python export functionality then challenged us with circular imports, environment setup, and maintaining compatibility with the existing architecture.

## Cross Platform Support (macOS) 
### macOS Accessibility Permission Warning:
When running PyMacroRecord on macOS, the application will open, but macOS may  show one of these messages in the terminal: 
1. AXIsProcessTrusted: false
2. This Process is not trusted! Input event monitoring will no be possible until it is added to accessibility clients.

After investigating these messages, we found they appear because macOS hasn't given Python permission to monitor keyboard and mouse input. Because the application still runs, it may look like it works properly, but recording may not be working correctly due to needing permission. Therefore to inform users, a permission warning in terminal was added.

**Example of macOS Warning:**

<img width="609" height="540" alt="Screenshot 2025-12-02 at 9 43 35 PM" src="https://github.com/user-attachments/assets/03a017a5-4034-4407-a18c-2a7dd0f72768" />

### macOS Theme Appearences:
PyMacroRecord runs on both Windows and mac, but Tkinter displays UI elements differently depending on the OS.
Our demo is shown on Windows, but features were tested on macOS as well. 

**Light** 

<img width="617" height="252" alt="Screenshot 2025-12-02 at 9 50 00 PM" src="https://github.com/user-attachments/assets/72f5cbbb-c8b9-41b5-819e-7fcfa50f8097" />

**Dark**

<img width="613" height="249" alt="Screenshot 2025-12-02 at 9 49 55 PM" src="https://github.com/user-attachments/assets/761e1581-83a3-41c1-9b3b-b14e04c5c867" />

**Neon Noir**

<img width="618" height="245" alt="Screenshot 2025-12-02 at 9 49 48 PM" src="https://github.com/user-attachments/assets/51f39239-a0f6-400d-92fa-ed9a585b25d7" />

**Space Berries**

<img width="621" height="254" alt="Screenshot 2025-12-02 at 9 49 43 PM" src="https://github.com/user-attachments/assets/4bd22f9d-f051-4c20-806b-5c78cadafa3c" />

**Jolly**

<img width="614" height="251" alt="Screenshot 2025-12-02 at 9 49 37 PM" src="https://github.com/user-attachments/assets/55ce6ab7-75a8-421d-a16e-b36aeaaab623" />

**Coffee**

<img width="614" height="247" alt="Screenshot 2025-12-02 at 9 49 31 PM" src="https://github.com/user-attachments/assets/42091813-a144-4266-bcb8-dac5615e5c06" />

**Forest**

<img width="615" height="248" alt="Screenshot 2025-12-02 at 9 49 21 PM" src="https://github.com/user-attachments/assets/551bb04a-2ec0-430b-b433-cacb97096639" />

## Takeaways
This project provided hands-on experience with:
- Contributing to **open source** projects
- **Team-based** development workflows
- Python **GUI** applications using tkinter
- Learning how licenses work
- File format conversion

