from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import subprocess
import os

class File:
    def __init__(self, name, type, dateModified, size):
        self.name = name
        self.type = type
        self.dateModified = dateModified
        self.size = size 

# Window setup ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
wn = Tk()
wnWidth = 500
wnHeight = 500
wn.geometry(f"{wnWidth}x{wnHeight}")
wn.title("FileSort 0.0.0a")
# Functions ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def iter_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            yield os.path.join(root, file)

def ScanFiles():
    print("Scanning...")
    file_dir = os.listdir(filedialog.askdirectory())
    x = 0
    for i in file_dir:
        textArea.insert(x, i)
        print(os.stat(i))
        x+=1
    

# Widgets -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bScanFiles = ttk.Button(text="Scan Dir", command=ScanFiles)
bScanFiles.grid(
    row=1, column=1, 
    ipadx=10, ipady=30,
    padx=30, pady=30
)

bAddRule = ttk.Button(text = "Add Rule")
bAddRule.grid(
    row=1, column=2, 
    ipadx=10, ipady=30,
    padx=30, pady=30
)
textArea = ttk.Entry(wn,width=100)
textArea.grid(row=1, column=3, ipadx=10, ipady=10, padx=30, pady=30)

# Menu Bar ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# menuBar = Menu(wn)

# pcmenu = Menu(menuBar, tearoff=0)
# pcmenu.add_command(label="Patch")
# menuBar.add_cascade(label="PC", menu=pcmenu)

# Finalization -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
wn.resizable(False, False)
wn.mainloop()