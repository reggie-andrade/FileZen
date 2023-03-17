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
## TODO: Rewrite function to just write to .csv
def ScanFiles(): # scans chosen directory and appends file object with info on file
    """ Scans chosen directory and appends"""
    fileObjects.clear()
    fileDirName = (filedialog.askdirectory())
    
    for root, subdirs, files in os.walk(fileDirName):
        #fileInfo = os.stat(f"{fileDirName}/{i}")
        #fileObjects.append(File(fileInfo, i))
        if files != []: # Checks if list is empty and doesn't add it to fileObjects list
            for file in files:
                fileInfo = os.stat(os.path.join(root,file))
                fileObjects.append(File(fileInfo, file))
    for i in fileObjects:
        Label(labelFrame, text=i.getInfo(), bg="red").grid()

def writeToLog(FileObjects):
    """Writes to CSV File to log for later to search easy"""

    with open("log.csv", "w", encoding="UTF-8") as log:
        log.writelines((file for file in FileObjects) + ",")
        log.writelines("\n")

def AddSortingOption():
    # New window setup
    wnSortOpt = Toplevel(wn)
    wnSortOpt.title("Add file sorting option")
    wnSortOptWidth = 600
    wnSortOptHeight = 350
    wnSortOpt.geometry(f"{wnSortOptWidth}x{wnSortOptHeight}")

    selectVar = StringVar()
    selection = ttk.Combobox(wnSortOpt, width=27, state="readonly", textvariable=selectVar)
    selectionOptions = (
        "Sort files based on name",
        "Sort files based on type",
        "Sort files based on date",
    )
    selection['values'] = selectionOptions
    selection.grid(column=1, row=1, padx=10, pady=10)

    ifConditionVar = StringVar()
    ifCondition = ttk.Combobox(wnSortOpt, width=27, state="disabled", textvariable=ifConditionVar)
    ifCondition.grid(column=1, row=2, padx=10, pady=40)

    conditionResultVar = StringVar()
    conditionResult = ttk.Combobox(wnSortOpt, width=27, state="disabled", textvariable=conditionResultVar)
    conditionResultOptions = (
        "Move file to desktop",
        "Move file to videos",
        "Move file to photos",
        "Move file to specific folder...",
    )
    conditionResult['values'] = conditionResultOptions
    conditionResult.grid(column=2, row=2, padx=10, pady=40)

    #TODO 1: Create an entrybox for when "Sort files based on name" is used
    #TODO 2: Create 3 comboboxes for selecting dates, with mindfulness of days in each month
    
    def SelectionUpdate(self):
        # Reset if condition selection every time a new sorting option is selected
        ifConditionVar.set("")
        ifCondition.set("")

        selectedSortOpt = selectVar.get()
        ifConditions1 = (
            "If file name starts with...",
            "If file name ends with...",
            "If file name contains...",
        )
        ifConditions2 = (
            "If file is an image...",
            "If file is a video...",
            "If file is a document (PDF)...",
            "If file is of specific type...",
        )
        ifConditions3 = (
            "If file was created before...",
            "If file was created after...",
            "If file was created on...",
        )

        # Update if condition based on selection, unlock if condition and condition result
        conditionResult['state'] = "readonly"
        ifCondition['state'] = "readonly"
        if selectedSortOpt == selectionOptions[0]:
            ifCondition['values'] = ifConditions1
        elif selectedSortOpt == selectionOptions[1]:
            ifCondition['values'] = ifConditions2
        elif selectedSortOpt == selectionOptions[2]:
            ifCondition['values'] = ifConditions3

    selection.bind("<<ComboboxSelected>>", SelectionUpdate)

# Frames
labelFrame = Frame(wn, width=100, height=100)
labelFrame.grid()

# Widgets -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bWriteFiles = ttk.Button(text="Write to log.csv", command=writeToLog)
bWriteFiles.grid(
    row=1, column=1,
    ipax=10, ipady=30,
    padx=30, pady=30
)

bScanFiles = ttk.Button(text="Scan Dir", command=ScanFiles)
bScanFiles.grid(
    row=2, column=1, 
    ipadx=10, ipady=30,
    padx=30, pady=30
)

bAddSortingOption = ttk.Button(text = "Add Rule", command=AddSortingOption)
bAddSortingOption.grid(
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
