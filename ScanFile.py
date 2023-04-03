from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os

def ScanFiles(fileObjs, txt, fileclass): # scans chosen directory and appends file object with info on file
    """ Scans chosen directory and appends"""
    if txt["state"] == "disabled":
        txt.configure(state="normal")
    fileObjs.clear()
    fileDirName = (filedialog.askdirectory())
    
    for root, subdirs, files in os.walk(fileDirName):
        #fileInfo = os.stat(f"{fileDirName}/{i}")
        #fileObjects.append(File(fileInfo, i))
        if files != []: # Checks if list is empty and doesn't add it to fileObjects list
            for file in files:
                fileInfo = os.stat(os.path.join(root,file))
                fileObjs.append(fileclass(fileInfo, file))
    for files in fileObjs:
        txt.insert(END, f"{files.getInfo()}\n")
    
    txt.configure(state="disabled")