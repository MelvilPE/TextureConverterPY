import FileManager

SPECIFIC_FILE = "dds.tex"
RESULT_FILE   = "RES.txt"

def ReceiveDataFromFilePath(filePath):
    file = open(filePath, "rb+")
    fileData = file.read()
    file.close()
    return fileData

def WriteDumpLineFromFileData(fileData):
    bufferListExtractedToSTR = str(list(fileData))
    FileManager.WriteBufferToFilePath(RESULT_FILE, bufferListExtractedToSTR.encode())

WriteDumpLineFromFileData(ReceiveDataFromFilePath(SPECIFIC_FILE))