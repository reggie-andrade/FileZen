from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkcalendar import Calendar
from datetime import date

def addSortingOption(toplevel):
    # Setup ------------------------------------------------------------------------------------------------------------

    # New window setup
    wnSortOpt = Toplevel(toplevel)
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

    # Bindings
    selection.bind("<<ComboboxSelected>>", ifSelectionUpdate)
    ifCondition.bind("<<ComboboxSelected>>", ifEntryUpdate)
    conditionResult.bind("<<ComboboxSelected>>", dirSelectUpdate)

    # Finalization
    wnSortOpt.resizable(False, False)
