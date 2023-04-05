from tkinter import *
from tkinter import filedialog
import os
import datetime

class File:
    def __init__(self, fileInfo, fileName):
        self.name = fileName
        self.type = fileInfo.st_mode
        self.dateModified = fileInfo.st_atime
    
    def getInfo(self):
        return ("Name: " + self.name, "Size: "+ str(self.type/10000) + " Kb", "Date Modified: " + datetime.datetime.fromtimestamp(self.dateModified).strftime('%m/%d/%Y %H:%M:%S %p'))

def ScanFiles(fileObjs, txt): # scans chosen directory and appends file object with info on file
    """ Scans chosen directory and appends"""
    if txt["state"] == "disabled":
        txt.configure(state="normal")
    fileObjs.clear()
    fileDirName = (filedialog.askdirectory())
    
    for root, subdirs, files in os.walk(fileDirName):
        if files != []: # Checks if list is empty and doesn't add it to fileObjects list
            for file in files:
                fileInfo = os.stat(os.path.join(root,file))
                fileObjs.append(File(fileInfo, file))
    for files in fileObjs:
        txt.insert(END, f"{files.getInfo()}\n")
    
    txt.configure(state="disabled")
