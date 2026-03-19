import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

DEVNULL = subprocess.DEVNULL

print("NotepadRewind - V1.0\n\nNotepadRewind allows you to replace the new Windows 11 Notepad with the classic Windows XP one.\n\nCreated by Fernando Guerrero Nuez (https://fernandoguerreronuez.com)\n")
print("NOTICE: NotepadRewind requires a copy of the Windows XP Notepad (notepad.exe) that you own legally. NotepadRewind does not distribute any Microsoft software.\n")

root = tk.Tk()
root.withdraw()

while True:
    pathtonotepad = filedialog.askopenfilename(
        title="Select the Windows XP notepad.exe file",
        filetypes=[("Executable files", "*.exe")]
    )
    if pathtonotepad:
        break
    print("No file selected, please try again.")

pathtonotepad = pathtonotepad.replace("/", "\\")
filename = os.path.basename(pathtonotepad)

print(f"Securing file: {pathtonotepad}")
securepath = os.environ["APPDATA"] + "\\NotepadRewind\\files"
os.makedirs(securepath, exist_ok=True)
subprocess.run(f"copy {pathtonotepad} {securepath}", shell=True, stdout=DEVNULL, stderr=DEVNULL)
print(f"File secured in: {securepath}")

print("Modifying .txt file association...")
subprocess.run(f'ftype txtfilelegacy={securepath}\\{filename} "%1"', shell=True, stdout=DEVNULL, stderr=DEVNULL)
print(".txt files will now open with the classic Notepad. You can also set NotepadRewind as the default app for other file extensions in Windows Settings.")

print("\nCreating Start Menu shortcut...")
subprocess.run('powershell -Command "$s = (New-Object -ComObject WScript.Shell).CreateShortcut(\\"$env:APPDATA\\Microsoft\\Windows\\Start Menu\\Programs\\NotepadRewind.lnk\\"); $s.TargetPath = \\"$env:APPDATA\\NotepadRewind\\files\\notepad.exe\\"; $s.Save()"', shell=True, stdout=DEVNULL, stderr=DEVNULL)
print("Start Menu shortcut created.")

messagebox.showinfo("NotepadRewind", "NotepadRewind has been installed successfully!\n\nEnjoy the classic Notepad!")
