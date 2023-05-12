import os
import SortingRules
import ScanFile
from send2trash import send2trash

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

def SortToDirectory(ruleList, fileList):
    for file in fileList:
        for rule in ruleList:
            resultOptions = (
                "Move file to desktop",
                "Move file to videos",
                "Move file to photos",
                "Move file to specific folder...",
                "Move file to recycling bin"
            )

            lastDir = ScanFile.GetLastDirectory()
            fileMatches = rule.DoesFileMatch(file, lastDir)
            result = rule.GetResult()

            print(str(fileMatches) + ": " + file)

            if fileMatches:
                if result == resultOptions[0]:
                    desktop = os.path.expanduser("~/Desktop").replace("\\", "/")
                    os.rename(lastDir + "/" + file, desktop + "/" + file)
                elif result == resultOptions[1]:
                    videos = os.path.expanduser("~/Videos").replace("\\", "/")
                    os.rename(lastDir + "/" + file, videos + "/" + file)
                elif result == resultOptions[2]:
                    photos = os.path.expanduser("~/Pictures").replace("\\", "/")
                    os.rename(lastDir + "/" + file, photos + "/" + file)
                elif result == resultOptions[3]:
                    os.rename(lastDir + "/" + file, rule.GetTargetDir() + "/" + file)
                elif result == resultOptions[4]:
                    path_to_delete = lastDir + "/" + file
                    path_to_delete = path_to_delete.replace("/", "\\")
                    send2trash(path_to_delete)
