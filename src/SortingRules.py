from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkcalendar import Calendar
from datetime import date
from PIL import Image

# TODO: Add 'ignore files based on...'
class SortingRule:
    def __init__(self, sortingOption, ifcondition, ext, date, result, directory):
        # Setup step variables
        self.count = 0
        # Checking step variables
        self.sortingOption = sortingOption
        self.ifcondition = ifcondition
        self.extension = ext
        self.date = date
        # Final step variables
        self.result = result
        self.directory = directory
    
    # Check if the passed file matches criteria of rule
    def DoesFileMatch(self, file):
        match = False

        baseOptions = (
            "Sort files based on name",
            "Sort files based on type",
            "Sort files based on date",
        )

        if self.sortingOption == baseOptions[0]:
            print("Sorting based on name")
            ifConditions = (
                "If file name starts with...",
                "If file name ends with...",
                "If file name contains...",
            )

            if self.ifcondition == ifConditions[0]:
                if file.name.startswith(self.extension):
                    match = True
            elif self.ifcondition == ifConditions[1]:
                if file.name[:-4].endswith(self.extension):
                    match = True
            elif self.ifcondition == ifConditions[2]:
                if self.extension in file.name:
                    match = True
        elif self.sortingOption == baseOptions[1]:
            print("Sorting based on type")
            ifConditions = (
                "If file is an image...",
                "If file is a video...",
                "If file is a document (PDF)...",
                "If file is of specific type...",
            )

            # if self.ifcondition == ifConditions[0]:
            #     if file.name.startswith(self.extension):
            #         match = True
            # elif self.ifcondition == ifConditions[1]:
                
            # elif self.ifcondition == ifConditions[2]:
            #     if file.name.endswith("pdf"):
            #         match = True
            # elif self.ifcondition == ifConditions[3]:
            #     if file.name.endswith(self.extension):
            #         match = True
        elif self.sortingOption == baseOptions[2]:
            print("Sorting based on date")

    def __str__(self):
        return (
            f"SORTINGRULE {self.count}\n sortingOption: {self.sortingOption}\n ifcondition: {self.ifcondition}\n extension: {self.extension}\n date: {self.date}\n result: {self.result}\n directory: {self.directory}"
        )
        
        

def addSortingOption(toplevel):
    # Setup ------------------------------------------------------------------------------------------------------------
    rule = None

    # New window setup
    wnSortOpt = Toplevel(toplevel)
    wnSortOpt.title("Add file sorting rule")
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
            dirSelect.grid(column=conditionGridInfo["column"] + 1, row=2, padx=10)
    
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
    selection = ttk.Combobox(wnSortOpt, width=27, state="readonly", textvariable=selectVar)
    selectionOptions = (
        "Sort files based on name",
        "Sort files based on type",
        "Sort files based on date",
    )
    selection['values'] = selectionOptions
    selection.grid(column=1, row=1, padx=10, pady=10)

    # If conditions dropdown based on primary selection
    ifConditionVar = StringVar()
    ifCondition = ttk.Combobox(wnSortOpt, width=27, state="disabled", textvariable=ifConditionVar)
    ifCondition.grid(column=1, row=2, padx=10, pady=40)

    # Condition result dropdown based on if condition
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

    # If condition entry box, only visible if using a specific if condition
    ifEntryVar = StringVar()
    ifConditionEntry = ttk.Entry(wnSortOpt, width=17, textvariable=ifEntryVar)

    # Directory select button, only shows if "Move file to specific folder" is used
    dirSelectVar = StringVar()
    dirSelect = ttk.Button(wnSortOpt, command=selectSpecificDir, textvariable=dirSelectVar)
    dirSelectVar.set("Select folder")

    # Visual calandar used for if primary selection is "Sort files based on date"
    todaysDate = date.today()
    cal = Calendar(wnSortOpt, selectmode="day", year=todaysDate.year, month=todaysDate.month, day=todaysDate.day)

    # Submit button
    submitVar = IntVar()
    submit = ttk.Button(wnSortOpt, command=lambda: submitVar.set(1))
    submit.configure(text="Submit")
    submit.grid(column=1, row=3, padx=10, pady=10)

    # Bindings
    selection.bind("<<ComboboxSelected>>", ifSelectionUpdate)
    ifCondition.bind("<<ComboboxSelected>>", ifEntryUpdate)
    conditionResult.bind("<<ComboboxSelected>>", dirSelectUpdate)

    # Finalization
    wnSortOpt.resizable(False, False)

    submit.wait_variable(submitVar)

    rule = SortingRule(
        selectVar.get(),
        ifConditionVar.get(),
        ifEntryVar.get(),
        cal.get_date(),
        conditionResultVar.get(),
        dirSelectVar.get()
    )

    wnSortOpt.destroy()
    return rule
