""" sorting functions (i'm not touching fucking anything in this! Just praying that it works (._.;)) """
import os
import datetime
from tkinter import filedialog

""" Files are passed through this class for accessibility"""


class File:
    fileObjects = []

    def __init__(self, fileInfo, fileName):
        self.name = fileName
        self.type = fileInfo.st_mode
        self.dateModified = fileInfo.st_atime

    def getInfo(self):
        return ("Name: " + self.name, "Size: " + str(self.type/10000) + " Kb", "Date Modified: " + datetime.datetime.fromtimestamp(self.dateModified).strftime('%m/%d/%Y %H:%M:%S %p'))

    """ Scans user chosen directory recursively, creates class (File) objects and inserts them into text box for user to view"""
    def scanDirectory():
        fileObjects = File.fileObjects
        fileObjects.clear()
        fileDirectoryName = (filedialog.askdirectory())

        for root, subdirs, files in os.walk(fileDirectoryName):
            if files != []:
                for file in files:
                    fileInfo = os.stat(os.path.join(root, file))
                    File.fileObjects.append(File(fileInfo, file))

    def writeToTextBox(self, textBox):
        fileObjects = File.fileObjects
        for objects in fileObjects:
            textBox.insert(f"{objects.getInfo()},\n")

    def writeToFile(fileObjects):
        """ Writes (File) objects to a file (most likely .csv) and formats it properly """
        with open("log.csv", "w", encoding="UTF-8") as log:
            for files in fileObjects:
                log.writelines(f"{files.getInfo()},\n")

        print("writeToFile completed")


""" Not even gonna bother (T-T) (This is reggie's *fix* for sorting files...) """


def addSortingOption(toplevel):
    # Setup ------------------------------------------------------------------------------------------------------------

    # New window setup
    wnSortOpt = CTkToplevel(toplevel)
    wnSortOpt.title("Add file sorting option")
    wnSortOptWidth = 1100
    wnSortOptHeight = 450
    wnSortOpt.geometry(f"{wnSortOptWidth}x{wnSortOptHeight}")

    # Functions ------------------------------------------------------------------------------------------------------------

    # Function to update if condition dropdown based on primary selection dropdown
    def ifSelectionUpdate(self):
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

        dirSelect.grid_forget()

        conditionResult.grid(column=2, row=2, padx=10, pady=40)

        # Get if statement selection, change if statement
        selectedSortOpt = selectVar.get()

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

    # Function to cause the directory selection button to appear if the condition result is "Move file to specific folder"
    def dirSelectUpdate(self):
        # Reset widgets
        dirSelect.grid_forget()
        dirSelectVar.set("Select folder")

        conditionSelect = conditionResultVar.get()
        conditionGridInfo = conditionResult.grid_info()

        if conditionSelect == "Move file to specific folder...":
            dirSelect.grid(
                column=conditionGridInfo["column"] + 1, row=2, padx=10)

    # Function to cause the if condition entry box to appear if any conditions are true
    def ifEntryUpdate(self):
        ifConditions1 = (
            "If file name starts with...",
            "If file name ends with...",
            "If file name contains...",
        )

        # Reset widgets
        ifConditionEntry.grid_forget()

        conditionResultVar.set("")
        conditionResult.set("")

        if ifConditionVar.get() == "If file is of specific type...":
            ifConditionEntry.grid(column=2, row=2, padx=10, pady=40)
            conditionResult.grid(column=3, row=2, padx=10, pady=40)
        else:
            for opt in ifConditions1:
                if ifConditionVar.get() == opt:
                    ifConditionEntry.grid(column=2, row=2, padx=10, pady=40)
                    conditionResult.grid(column=3, row=2, padx=10, pady=40)

    # Function to select a specific directory, used if condition result "Move file to specific folder" is used
    def selectSpecificDir():
        selectedFolder = filedialog.askdirectory()
        dirSelectVar.set(selectedFolder)
        wnSortOpt.lift()

    # Widgets ------------------------------------------------------------------------------------------------------------

    # Primary selection dropdown for file sorting
    selectVar = StringVar()
    selection = CTkComboBox(wnSortOpt, width=27,
                            state="readonly", textvariable=selectVar)
    selectionOptions = (
        "Sort files based on name",
        "Sort files based on type",
        "Sort files based on date",
    )
    selection['values'] = selectionOptions
    selection.grid(column=1, row=1, padx=10, pady=10)

    # If conditions dropdown based on primary selection
    ifConditionVar = StringVar()
    ifCondition = CTkComboBox(
        wnSortOpt, width=27, state="disabled", textvariable=ifConditionVar)
    ifCondition.grid(column=1, row=2, padx=10, pady=40)

    # Condition result dropdown based on if condition
    conditionResultVar = StringVar()
    conditionResult = CTkComboBox(
        wnSortOpt, width=27, state="disabled", textvariable=conditionResultVar)
    conditionResultOptions = (
        "Move file to desktop",
        "Move file to videos",
        "Move file to photos",
        "Move file to specific folder...",
        "Move file to recycling bin"
    )
    conditionResult['values'] = conditionResultOptions
    conditionResult.grid(column=2, row=2, padx=10, pady=40)

    # If condition entry box, only visible if using a specific if condition
    ifEntryVar = StringVar()
    ifConditionEntry = CTkEntry(wnSortOpt, width=17, textvariable=ifEntryVar)

    # Directory select button, only shows if "Move file to specific folder" is used
    dirSelectVar = StringVar()
    dirSelect = CTkButton(
        wnSortOpt, command=selectSpecificDir, textvariable=dirSelectVar)
    dirSelectVar.set("Select folder")

    # Visual calandar used for if primary selection is "Sort files based on date"
    todaysDate = date.today()
    cal = Calendar(wnSortOpt, selectmode="day", year=todaysDate.year,
                   month=todaysDate.month, day=todaysDate.day)

    # Bindings
    selection.bind("<<ComboboxSelected>>", ifSelectionUpdate)
    ifCondition.bind("<<ComboboxSelected>>", ifEntryUpdate)
    conditionResult.bind("<<ComboboxSelected>>", dirSelectUpdate)

    # Finalization
    wnSortOpt.resizable(False, False)
