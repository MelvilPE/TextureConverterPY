import FileManager
import PVRManager

ARGS = {"convertedFolder": "erlenberg", "generateTex": True}

def ConvertToAnyFormat(originalExtension, editedExtension):
    originalFilePaths = FileManager.FilterFilePathsWithExt(FileManager.CollectFilePathsList(ARGS["convertedFolder"]), originalExtension)
    for eachTexture in originalFilePaths:
        texFilePath = eachTexture
        texFilePath = eachTexture.replace(originalExtension, ".tex")

        # Transform to packed format
        if ".png" in originalExtension:
            PVRManager.ConvertFormatPNGToPacked(eachTexture, editedExtension)
        
        # Transform to unpacked format
        if ".png" in editedExtension:
            PVRManager.ConvertFormatPackedToPNG(eachTexture)
        
        if ARGS["generateTex"]:
            PVRManager.WriteTexForFormat(texFilePath, originalExtension, editedExtension)

        print("Conversion from", originalExtension, "to", editedExtension, "finished", eachTexture)

    FileManager.DeleteAllFilesOfExtInDirectory(ARGS["convertedFolder"], originalExtension)
    FileManager.DeleteAllFilesOfExtInDirectory(ARGS["convertedFolder"], ".mali_Out.pvr")
        

def TextureConverter():
    # Cleaning up all Tex Files
    FileManager.DeleteAllFilesOfExtInDirectory(ARGS["convertedFolder"], ".tex")
    ConvertToAnyFormat(".dx11.dds", ".mali.pvr")

if __name__ == '__main__':
    TextureConverter()
