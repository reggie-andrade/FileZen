import os
import SortingRules

def stripExtension(fileName):
    splitfileName = fileName.split(".")
    fileName=""

    if len(splitfileName) > 2:
        for i in range(len(splitfileName)-2):
            fileName += splitfileName[i] + "."

        fileName += splitfileName[-2]
    else:
        fileName = splitfileName[0]

    return fileName

def isImage(fileName):
    images = ["png", "jpg", "psd", "jpeg", "TIFF", "bmp"]

    if fileName.split(".")[-1] in images:
        return True
    else:
        return False
    
def isVideo(fileName):
    videos = ["webm", "mkv", "flv", "mpg", "mpeg", "mp4", "m4v", "gif", "MTS", "M2TS", "TS"]

    if fileName.split(".")[-1] in videos:
        return True
    else:
        return False


def isExtension(fileName, ext):
    if fileName.split(".")[-1] == ext:
        return True
    else:
        return False

def SortToDesktop(ruleList, fileList):
    print("ran SortToDesktop")
    for file in fileList:
        for rule in ruleList:
            print(str(rule.DoesFileMatch(file)) + ": " + file)
