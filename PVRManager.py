import LoggerErrors as Logger
import FileManager
import PVRManager
import subprocess

TEX_MALI_PVR = bytes([0, 238, 238, 0, 8, 1, 1, 1, 5, 1, 3, 18, 0])
TEX_DX11_PVR = bytes([0, 238, 238, 0, 13, 0, 0, 1, 1, 2, 1, 0, 0, 46, 112, 110, 103, 0, 0, 5, 2, 6])

TEX_DX11_DDS = bytes([0, 238, 238, 0, 13, 0, 0, 1, 1, 2, 1, 0, 4, 46, 116, 103, 97, 0, 0, 5, 1, 16])
TEX_ORIG_DDS = bytes([238, 0, 238, 0, 13, 0, 0, 1, 1, 2, 1, 0, 1, 46, 100, 100, 115, 0, 7, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
TEX_ORIG_PNG = bytes([238, 0, 238, 0, 13, 0, 0, 1, 1, 2, 1, 0, 0, 46, 112, 110, 103, 0, 7, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 127, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def RunCommandWithoutPopingConsole(cmd):
    si = subprocess.STARTUPINFO()
    si.wShowWindow = subprocess.SW_HIDE
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.call(cmd, startupinfo=si)

def WriteTexForFormat(texFilePath, editedExtension):
    if ".dds" in editedExtension:
        if ".dx11" in editedExtension:
            FileManager.WriteBufferToFilePath(texFilePath, PVRManager.TEX_DX11_DDS)
        else:
            FileManager.WriteBufferToFilePath(texFilePath, PVRManager.TEX_ORIG_DDS)

    if ".pvr" in editedExtension:
        if ".dx11" in editedExtension:
            FileManager.WriteBufferToFilePath(texFilePath, PVRManager.TEX_DX11_PVR)
        elif ".mali" in editedExtension:
            FileManager.WriteBufferToFilePath(texFilePath, PVRManager.TEX_MALI_PVR)
        else:
            Logger.Error("Unsupported type of PVR GPU!")

    if ".png" in editedExtension:
        FileManager.WriteBufferToFilePath(texFilePath, PVRManager.TEX_ORIG_PNG)

def ConvertFormatPackedToPNG(packedTexture):
    pngTexture = packedTexture
    if ".dds" in packedTexture:
        if ".dx11" in packedTexture:
            pngTexture = packedTexture.replace(".dx11.dds", ".png")
        else:
            pngTexture = packedTexture.replace(".dds", ".png")

    elif ".pvr" in packedTexture:
        if ".dx11" in packedTexture:
            pngTexture = packedTexture.replace(".dx11.pvr", ".png")
        elif ".mali" in packedTexture:
            pngTexture = packedTexture.replace(".mali.pvr", ".png")
        else:
            Logger.Error("Unsupported type of PVR GPU!")
    else:
        Logger.Error("Unsupported type of texture")

    RunCommandWithoutPopingConsole("PVRTexToolCLI -f r8g8b8a8 -i \"" + packedTexture + "\" -d \"" + pngTexture + "\"")

def ConvertFormatPNGToPacked(pngTexture, newExtension):
    packedTexture = pngTexture
    packedTexture = packedTexture.replace(".png", newExtension)
    RunCommandWithoutPopingConsole("PVRTexToolCLI -f r8g8b8a8 -i \"" + pngTexture + "\" -o \"" + packedTexture + "\"")