import SortingRules
import ScanFile
import Sort
import tkinter
import customtkinter as cstk
from SortingRules import SortingRule

fileObjects = []
rules = []

# Window setup ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

cstk.set_appearance_mode("dark") 
cstk.set_default_color_theme("C:/Users/Karat/OneDrive/Desktop/FileSort/FileSort-main/src/theme.json")

wnWidth = 530
wnHeight = 280
wn = cstk.CTk()
wn.geometry(f"{wnWidth}x{wnHeight}")
wn.title("FileSort 1.0.0")

# Functions ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def ScanFiles():
    global fileObjects
    fileObjects = ScanFile.ScanFiles(fileObjects)
        
# Adds a sorting option which the user can use to dictate how their directory of choice will be organized
ruleCount = 0
def addSortOpt():
    global ruleCount
    wn.lower()
    r = SortingRules.addSortingOption(wn)
    r.count = ruleCount
    ruleCount += 1
    rules.append(r)
    print(r)

# Runs the Sort module to sort files
def SortFiles(ruleList, fileList):
    print("Files:")
    for file in fileList:
        print(file)
    
    print("Rules:")
    for rule in ruleList:
        print(rule)
    
    Sort.SortToDirectory(ruleList, fileList)

# Widgets -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bScanFiles = cstk.CTkButton(master=wn, text="Select Folder", command=ScanFiles)
bScanFiles.grid(
    row=1, column=1, 
    ipadx=10, ipady=10,
    padx=30, pady=30
)

txtScanFiles = cstk.CTkLabel(master=wn, text="1. Select the folder you'd like to auto-sort", fg_color="transparent", justify="left")
txtScanFiles.grid(
    row=1, column=2, 
)

bAddSortingOption = cstk.CTkButton(master=wn, text = "Add Rule", command=addSortOpt)
bAddSortingOption.grid(
    row=2, column=1, 
    ipadx=10, ipady=10,
)

txtSortingOption = cstk.CTkLabel(master=wn, text="2. Add as many rules as you need to sort the folder", fg_color="transparent", justify="left")
txtSortingOption.grid(
    row=2, column=2, 
)

bSort = cstk.CTkButton(master=wn, text="Sort!", command=lambda:SortFiles(rules, fileObjects))
bSort.grid(
    row=3, column=1,
    ipadx=10, ipady=10,
    padx=30, pady=30
)

txtSort = cstk.CTkLabel(master=wn, text="3. Sort your files!", fg_color="transparent", justify="left")
txtSort.grid(
    row=3, column=2, 
)

# Window -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

wn.mainloop()
