from tkinter import *
from tkinter import filedialog
import os
import datetime

lastDirectory = None

def ScanFiles(fileObjs):
    fileDir = (filedialog.askdirectory())
    fileObjs = os.listdir(fileDir)

    for file in fileObjs:
        if not "." in file:
            fileObjs.remove(file)

    global lastDirectory
    lastDirectory = fileDir

    return fileObjs

def GetLastDirectory():
    return lastDirectory
