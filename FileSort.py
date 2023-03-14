from tkinter import *
from tkinter import ttk
import os

# Window setup ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
wn = Tk()
wnWidth = 900
wnHeight = 500
wn.geometry(f"{wnWidth}x{wnHeight}")
wn.title("FileSort 1.0.0a")

# Functions ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def iter_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            yield os.path.join(root, file)

def ScanFiles():
    print("Scanning...")

# Widgets -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bScanFiles = ttk.Button(text="Scan Files", command=ScanFiles)
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

# Menu Bar ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# menuBar = Menu(wn)

# pcmenu = Menu(menuBar, tearoff=0)
# pcmenu.add_command(label="Patch")
# menuBar.add_cascade(label="PC", menu=pcmenu)

# Finalization -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
wn.resizable(False, False)
wn.mainloop()