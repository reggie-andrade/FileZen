from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import datetime
import os

class File:
    def __init__(self, fileInfo, fileName):
        self.name = fileName
        self.type = fileInfo.st_mode
        self.dateModified = fileInfo.st_atime
    
    def getInfo(self):
        return ("Name: " + self.name, "Size: "+ str(self.type/10000) + " Kb", "Date Modified: " + datetime.datetime.fromtimestamp(self.dateModified).strftime('%m/%d/%Y %H:%M:%S %p'))

# Window setup ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
fileObjects = []

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

def ScanFiles(): # scans chosen directory and appends file object with info on file
    fileObjects.clear()
    fileDirName = (filedialog.askdirectory())
    print("This is filedirname " + fileDirName)
    fileDirContents = os.listdir(fileDirName)
    
    for root, subdirs, files in os.walk(fileDirContents):
        fileInfo = os.stat(f"{fileDirName}/{i}")
        fileObjects.append(File(fileInfo, i))
    
    for i in fileObjects:
        Label(labelFrame, text=i.getInfo(), bg="red").grid()
    


# Frames
labelFrame = Frame(wn, width=100, height=100)
labelFrame.grid()

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
#wn.resizable(False, False)
wn.mainloop()