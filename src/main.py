import SortingOptions
import ScanFile
from tkinter import *
from tkinter import ttk

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
    ScanFile.ScanFiles(fileObjects, text)

def writeToLog(FileObjects):
    """Writes to CSV File to log for later to search easy"""
    with open("log.csv", "w", encoding="UTF-8") as log:
       for files in FileObjects:
            log.writelines(str(files.getInfo()) + ",\n")
        
# Adds a sorting option which the user can use to dictate how their directory of choice will be organized
def addSortOpt():
    SortingOptions.addSortingOption(wn)

# Widgets -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

labelFrame = Frame(wn, width=100, height=100)
labelFrame.grid()

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

bAddSortingOption = ttk.Button(text = "Add Rule", command=addSortOpt)
bAddSortingOption.grid(
    row=1, column=2, 
    ipadx=10, ipady=30,
    padx=30, pady=30
)

entryBoxScrollbar = Scrollbar(labelFrame)
entryBoxScrollbar.pack(side=RIGHT, fill=Y)

text = Text(labelFrame, yscrollcommand=entryBoxScrollbar.set)
text.pack(side=LEFT, fill=BOTH, expand=True)

# Window -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

wn.mainloop()
