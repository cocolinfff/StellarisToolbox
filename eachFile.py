import os


def eachFile(filepath):
    fileList = []
    pathDir = os.walk(filepath)
    for allDir in pathDir:
        for files in allDir[2]:
            fileList.append(allDir[0]+'\\'+files)
    return fileList



