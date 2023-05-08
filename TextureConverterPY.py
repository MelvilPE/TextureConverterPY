import FileManager
import PVRManager
import LoggerErrors as Logger

ARGS = {
    "convertedFolder": "erlenberg",
    "generateTex": True,
    "originalExtension": ".mali.pvr",
    "editedExtension": ".png"
}

def ConvertToAnyFormat(originalExtension, editedExtension):
    originalFilePaths = FileManager.FilterFilePathsWithExt(FileManager.CollectFilePathsList(ARGS["convertedFolder"]), originalExtension)
    for eachTexture in originalFilePaths:
        texFilePath = eachTexture
        texFilePath = eachTexture.replace(originalExtension, ".tex")
        
        if not ".png" in originalExtension and not ".png" in editedExtension:
            Logger.Error("PNG Extension not found in both formats, Please insert intermediate PNG format", [originalExtension, editedExtension])

        # Transform to packed format
        if ".png" in originalExtension:
            PVRManager.ConvertFormatPNGToPacked(eachTexture, editedExtension)
        
        # Transform to unpacked format
        if ".png" in editedExtension:
            PVRManager.ConvertFormatPackedToPNG(eachTexture)
        
        if ARGS["generateTex"]:
            PVRManager.WriteTexForFormat(texFilePath, editedExtension)

        print("Conversion from", originalExtension, "to", editedExtension, "finished", eachTexture)

    FileManager.DeleteAllFilesOfExtInDirectory(ARGS["convertedFolder"], originalExtension)
    FileManager.DeleteAllFilesOfExtInDirectory(ARGS["convertedFolder"], ".mali_Out.pvr")
    FileManager.DeleteAllFilesOfExtInDirectory(ARGS["convertedFolder"], ".dx11_Out.pvr")
    
def TextureConverter():
    FileManager.DeleteAllFilesOfExtInDirectory(ARGS["convertedFolder"], ".tex")
    ConvertToAnyFormat(ARGS["originalExtension"], ARGS["editedExtension"])
    print("(Debug) Finished to convert every textures")
    
if __name__ == '__main__':
    TextureConverter()
