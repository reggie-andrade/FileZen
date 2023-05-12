import customtkinter
from sorting import File

class TextFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side='bottom', fill='x')

        self.text = customtkinter.CTkTextbox(self,  height=200)
        self.text.pack(side='bottom', fill='x', expand=True)

    def scanDirectory(self, fileObjects, textBoxWidget):
        fileObjects.clear()
        fileDirectoryName = (filedialog.askdirectory())

        for root, subdirs, files in os.walk(fileDirectoryName):
            if files != []:
                for file in files:
                    fileInfo = os.stat(os.path.join(root, file))
                    File.fileObjects.append(File(fileInfo, file))

        for files in File.fileObjects:
            textBoxWidget.insert(END, f"{files.getInfo()}\n")


class ButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.pack(side='left', fill='y')
        self.paddingX = 3
        self.paddingY = 3

        self.optionsLabel = customtkinter.CTkLabel(self, text="Options", bg_color="#1f6aa5")
        self.optionsLabel.pack(side='top', fill='x')

        self.scanFiles = customtkinter.CTkButton(self, text="Select Directory", command=File.scanDirectory)
        self.scanFiles.pack(pady=self.paddingX)

        self.writeFiles = customtkinter.CTkButton(self, text="Write to history", command=lambda: File.writeToFile)
        self.writeFiles.pack(pady=self.paddingX)

        self.addSortingRule = customtkinter.CTkButton(self, text="Add Sorting Rule")
        self.addSortingRule.pack(pady=self.paddingX)

        self.sort = customtkinter.CTkButton(self, text="Sort Files!")
        self.sort.pack(side='bottom', pady=self.paddingY)


class Root(customtkinter.CTk):  # Root window, should only be called once
    def __init__(self):
        # root window setup
        super().__init__()
        customtkinter.set_appearance_mode("dark")

        self.windowWidth = 500
        self.windowHeight = 500
        self.title("File Sort Application (ab28814 implementation)")
        self.geometry(f"{self.windowWidth}x{self.windowHeight}")

        self.buttonFrame = ButtonFrame(self)
        self.textFrame = TextFrame(self)

        self.writeFiles = customtkinter.CTkButton(self, text="Write to history")

        self.wm_resizable(False, False)
    
    def getTextBox(self):
        return self.textFrame
