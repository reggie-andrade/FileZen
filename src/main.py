from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkcalendar import Calendar
from datetime import date
import datetime
import os

class File:
    def __init__(self, fileInfo, fileName):
        self.name = fileName
        self.type = fileInfo.st_mode
        self.dateModified = fileInfo.st_atime
    
    def getInfo(self):
        return ("Name: " + self.name, "Size: "+ str(self.type/10000) + " Kb", "Date Modified: " + datetime.datetime.fromtimestamp(self.dateModified).strftime('%m/%d/%Y %H:%M:%S %p'))

fileObjects = []
# Window setup ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
wnWidth = 850 
wnHeight = 850 


wn = Tk()
wn.geometry(f"{wnWidth}x{wnHeight}")
wn.title("FileSort 0.0.0a")
# Functions ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## TODO: Rewrite function to just write to .csv
def ScanFiles(): # scans chosen directory and appends file object with info on file
    """ Scans chosen directory and appends"""
    if text["state"] == "disabled":
        text.configure(state="normal")
    fileObjects.clear()
    fileDirName = (filedialog.askdirectory())
    
    for root, subdirs, files in os.walk(fileDirName):
        #fileInfo = os.stat(f"{fileDirName}/{i}")
        #fileObjects.append(File(fileInfo, i))
        if files != []: # Checks if list is empty and doesn't add it to fileObjects list
            for file in files:
                fileInfo = os.stat(os.path.join(root,file))
                fileObjects.append(File(fileInfo, file))
    for files in fileObjects:
        text.insert(END, f"{files.getInfo()}\n")
    
    text.configure(state="disabled")

def writeToLog(FileObjects):
    """Writes to CSV File to log for later to search easy"""
    with open("log.csv", "w", encoding="UTF-8") as log:
       # log.writelines((file for file in FileObjects) + ",")
       for files in FileObjects:
            log.writelines(str(files.getInfo()) + ",\n")
        

def addSortingOption():
    # New window setup
    wnSortOpt = Toplevel(wn)
    wnSortOpt.title("Add file sorting option")
    wnSortOptWidth = 850
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
        "Move file to recycling bin"
    )
    conditionResult['values'] = conditionResultOptions
    conditionResult.grid(column=2, row=2, padx=10, pady=40)

    ifEntryVar = StringVar()
    ifConditionEntry = ttk.Entry(wnSortOpt, width=17)

    def selectSpecificDir():
        selectedFolder = filedialog.askdirectory()

    dirSelect = ttk.Button(wnSortOpt, text="Select Folder", command=selectSpecificDir)
    dirEntry = ttk.Entry(wnSortOpt, width=25, state="readonly")

    # 3 comboboxes for selecting dates, with mindfulness of days in each month
    todaysDate = date.today()
    cal = Calendar(wnSortOpt, selectmode="day", year=todaysDate.year, month=todaysDate.month, day=todaysDate.day)
    
    def ifSelectionUpdate(self):
        # Reset widgets
        ifConditionVar.set("")
        ifCondition.set("")

        conditionResultVar.set("")
        conditionResult.set("")

        ifEntryVar.set("")
        ifConditionEntry.delete(0, END)
        ifConditionEntry.grid_forget()

        cal.grid_forget()
        cal.selection_set(todaysDate)

        conditionResult.grid(column=2, row=2, padx=10, pady=40)

        # Get if statement selection, change if statement
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
            ifConditionEntry.grid(column=2, row=2, padx=10, pady=40)
            conditionResult.grid(column=3, row=2, padx=10, pady=40)
        elif selectedSortOpt == selectionOptions[1]:
            ifCondition['values'] = ifConditions2
        elif selectedSortOpt == selectionOptions[2]:
            ifCondition['values'] = ifConditions3
            cal.grid(column=2, row=2, padx=10, pady=40)
            conditionResult.grid(column=3, row=2, padx=10, pady=40)

    selection.bind("<<ComboboxSelected>>", ifSelectionUpdate)
    wnSortOpt.resizable(False, False)
    
# Frames
labelFrame = Frame(wn, width=100, height=100)
labelFrame.grid()

# Widgets -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bWriteFiles = ttk.Button(text="Write to log.csv", command=lambda:writeToLog(fileObjects)) 
bWriteFiles.grid(
    row=1, column=1,
    ipadx=10, ipady=30,
    padx=30, pady=30
)

bScanFiles = ttk.Button(text="Scan Dir", command=ScanFiles)
bScanFiles.grid(
    row=2, column=1, 
    ipadx=10, ipady=30,
    padx=30, pady=30
)

bAddSortingOption = ttk.Button(text = "Add Rule", command=addSortingOption)
bAddSortingOption.grid(
    row=1, column=2, 
    ipadx=10, ipady=30,
    padx=30, pady=30
)

entryBoxScrollbar = Scrollbar(labelFrame)
entryBoxScrollbar.pack(side=RIGHT, fill=Y)

text = Text(labelFrame, yscrollcommand=entryBoxScrollbar.set)
text.pack(side=LEFT, fill=BOTH, expand=True)

# Menu Bar ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# menuBar = Menu(wn)

# pcmenu = Menu(menuBar, tearoff=0)
# pcmenu.add_command(label="Patch")
# menuBar.add_cascade(label="PC", menu=pcmenu)

# Finalization -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#wn.resizable(False, False)
wn.mainloop()
