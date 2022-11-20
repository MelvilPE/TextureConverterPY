import os

def WriteBufferToFilePath(filePath, buffer):
    stream = open(filePath, "wb")
    stream.write(buffer)
    stream.close()

def CollectFilePathsList(directory):
    filePathList = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            filePathList.append(os.path.join(root,file))
            
    return filePathList

def FilterFilePathsWithExt(filePathList, extension):
    filteredList = []
    for eachFilePath in filePathList:
        if extension in eachFilePath:
            filteredList.append(eachFilePath)
    return filteredList

def DeleteFileFromFilePath(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)

def DeleteAllFilesOfExtInDirectory(directory, extension):
    filePathList = CollectFilePathsList(directory)
    for eachFilePath in filePathList:
        if extension in eachFilePath:
            DeleteFileFromFilePath(eachFilePath)