import tkinter
import customtkinter as cstk
import datetime as dt
import time
import os
import Sort

# TODO: Add 'ignore files based on...'
class SortingRule:
    def __init__(self, sortingOption, ifcondition, entry, result, directory):
        # Setup step variables
        self.count = 0
        # Checking step variables
        self.sortingOption = sortingOption
        self.ifcondition = ifcondition
        self.entry = entry
        # Final step variables
        self.result = result
        self.directory = directory
    
    # Check if the passed file matches criteria of rule
    def DoesFileMatch(self, fileName, fileDir):
        match = False

        baseOptions = (
            "Sort files based on name",
            "Sort files based on type",
            "Sort files based on date",
        )

        if self.sortingOption == baseOptions[0]:
            ifConditions = (
                "If file name starts with...",
                "If file name ends with...",
                "If file name contains...",
            )

            if self.ifcondition == ifConditions[0]:
                if fileName.startswith(self.entry):
                    match = True
            elif self.ifcondition == ifConditions[1]:
                if Sort.stripExtension(fileName).endswith(self.entry):
                    match = True
            elif self.ifcondition == ifConditions[2]:
                if self.entry in fileName:
                    match = True
        elif self.sortingOption == baseOptions[1]:
            ifConditions = (
                "If file is an image...",
                "If file is a video...",
                "If file is a document (PDF)...",
                "If file is of specific type...",
            )

            if self.ifcondition == ifConditions[0]:
                if Sort.isImage(fileName):
                    match = True
            elif self.ifcondition == ifConditions[1]:
                if Sort.isVideo(fileName):
                    match = True
            elif self.ifcondition == ifConditions[2]:
                if Sort.isExtension(fileName, "pdf"):
                    match = True
            elif self.ifcondition == ifConditions[3]:
                if Sort.isExtension(fileName, self.entry):
                    match = True
        elif self.sortingOption == baseOptions[2]:
            ifConditions = (
                "If file was created before...",
                "If file was created after...",
                "If file was created on...",
            )

            givenDate = dt.datetime.strptime(self.entry, "%m/%d/%Y")
            creationDate = dt.datetime.fromtimestamp(os.path.getctime(fileDir + "/" + fileName))
            creationDate = creationDate.replace(hour=0, minute=0, second=0, microsecond=0)

            if self.ifcondition == ifConditions[0]:
                if creationDate < givenDate:
                    match = True
            elif self.ifcondition == ifConditions[1]:
                if creationDate > givenDate:
                    match = True
            elif self.ifcondition == ifConditions[2]:
                if creationDate == givenDate:
                    match = True
        return match

    def GetResult(self):
        return self.result
    
    def GetTargetDir(self):
        return self.directory
    
    def __str__(self):
        return (
            f"SORTINGRULE {self.count}\n sortingOption: {self.sortingOption}\n ifcondition: {self.ifcondition}\n entry: {self.entry}\n result: {self.result}\n directory: {self.directory}"
        )
        


def addSortingOption(toplevel):
    # Setup ------------------------------------------------------------------------------------------------------------
    rule = None

    # New window setup
    cstk.set_appearance_mode("dark") 
    cstk.set_default_color_theme("C:/Users/Karat/OneDrive/Desktop/FileSort/FileSort-main/src/theme.json")

    wnSortOpt = cstk.CTkToplevel()
    wnSortOpt.title("Add file sorting rule")
    wnSortOptWidth = 800
    wnSortOptHeight = 350
    wnSortOpt.geometry(f"{wnSortOptWidth}x{wnSortOptHeight}")
    wnSortOpt.attributes("-topmost", True)

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
        ifCondition.set("")

        conditionResult.set("")

        caseEntryVar.set("")
        caseEntry.delete(0, cstk.END)
        caseEntry.grid_forget()

        dirSelect.grid_forget()

        conditionResult.grid(column=2, row=2, padx=10, pady=40)

        # Get if statement selection, change if statement
        selectedSortOpt = selection.get()

        # Update if condition based on selection, unlock if condition and condition result
        conditionResult.configure(state = "readonly")
        ifCondition.configure(state = "readonly")

        if selectedSortOpt == selectionOptions[0]:
            ifCondition.configure(values = ifConditions1)
            caseEntry.grid(column=2, row=2, padx=10, pady=40)
            conditionResult.grid(column=3, row=2, padx=10, pady=40)
        elif selectedSortOpt == selectionOptions[1]:
            ifCondition.configure(values = ifConditions2)
        elif selectedSortOpt == selectionOptions[2]:
            ifCondition.configure(values = ifConditions3)
            caseEntry.grid(column=2, row=2, padx=10, pady=40)
            caseEntry.insert(0, "O/OO/OOOO")
            conditionResult.grid(column=3, row=2, padx=10, pady=40)

    # Function to cause the directory selection button to appear if the condition result is "Move file to specific folder"
    def dirSelectUpdate(self):
        # Reset widgets
        dirSelect.grid_forget()
        dirSelectVar.set("Select folder")

        conditionSelect = conditionResult.get()
        conditionGridInfo = conditionResult.grid_info()

        if conditionSelect == "Move file to specific folder...":
            dirSelect.grid(column=conditionGridInfo["column"] + 1, row=2, padx=10)
    
    # Function to cause the if condition entry box to appear if any conditions are true
    def ifEntryUpdate(self):
        # Reset widgets
        caseEntry.grid_forget()

        conditionResult.set("")
        
        if ifCondition.get() == "If file is of specific type...":
            caseEntry.grid(column=2, row=2, padx=10, pady=40)
            conditionResult.grid(column=3, row=2, padx=10, pady=40)
        elif selection.get() == "Sort files based on date":
            caseEntry.grid(column=2, row=2, padx=10, pady=40)
            caseEntry.delete(0, cstk.END)
            caseEntry.insert(0, "O/OO/OOOO")
            conditionResult.grid(column=3, row=2, padx=10, pady=40) 
        elif selection.get() == "Sort files based on name":
            caseEntry.grid(column=2, row=2, padx=10, pady=40)
            conditionResult.grid(column=3, row=2, padx=10, pady=40)
    
    # Function to select a specific directory, used if condition result "Move file to specific folder" is used
    def selectSpecificDir():
        wnSortOpt.attributes("-topmost", False)
        selectedFolder = cstk.filedialog.askdirectory()
        dirSelectVar.set(selectedFolder)
        wnSortOpt.attributes("-topmost", True)

    # Widgets ------------------------------------------------------------------------------------------------------------

    # Primary selection dropdown for file sorting
    
    selection = cstk.CTkComboBox(wnSortOpt, width=180, state="readonly", command=ifSelectionUpdate)
    selectionOptions = (
        "Sort files based on name",
        "Sort files based on type",
        "Sort files based on date",
    )
    selection.configure(values = selectionOptions)
    selection.grid(column=1, row=1, padx=10, pady=10)

    # If conditions dropdown based on primary selection
    ifCondition = cstk.CTkComboBox(wnSortOpt, width=180, state="disabled", command=ifEntryUpdate)
    ifCondition.grid(column=1, row=2, padx=10, pady=40)

    # Condition result dropdown based on if condition
    conditionResult = cstk.CTkComboBox(wnSortOpt, width=180, state="disabled")
    conditionResultOptions = (
        "Move file to desktop",
        "Move file to videos",
        "Move file to photos",
        "Move file to specific folder...",
        "Move file to recycling bin"
    )
    conditionResult.configure(values = conditionResultOptions, command=dirSelectUpdate)
    conditionResult.grid(column=2, row=2, padx=10, pady=40)

    # Entry box, only visible if using a specific if condition
    caseEntryVar = cstk.StringVar()
    caseEntry = cstk.CTkEntry(wnSortOpt, width=150, textvariable=caseEntryVar)

    # Directory select button, only shows if "Move file to specific folder" is used
    dirSelectVar = cstk.StringVar()
    dirSelect = cstk.CTkButton(wnSortOpt, command=selectSpecificDir, textvariable=dirSelectVar)
    dirSelectVar.set("Select folder")

    # Submit button
    submitVar = cstk.IntVar()
    submit = cstk.CTkButton(wnSortOpt, command=lambda: submitVar.set(1))
    submit.configure(text="Submit")
    submit.grid(column=1, row=3, padx=10, pady=10)

    # Finalization
    wnSortOpt.resizable(False, False)

    submit.wait_variable(submitVar)

    rule = SortingRule(
        selection.get(),
        ifCondition.get(),
        caseEntryVar.get(),
        conditionResult.get(),
        dirSelectVar.get()
    )

    wnSortOpt.destroy()
    return rule
