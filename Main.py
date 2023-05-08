import os
import customtkinter
customtkinter.set_appearance_mode("dark")  # system (default), light, dark
customtkinter.set_default_color_theme("blue")  # blue (default), dark-blue, green

import TextureConverterPY as TextureConverter

def TextureConverterExec():
    TextureConverter.ARGS = {
        "convertedFolder": textBoxPath.get(1.0, "end-1c"),
        "generateTex": bool(isTexCheckBox.get()),
        "originalExtension": textBoxOriginal.get(1.0, "end-1c"),
        "editedExtension": textBoxEdited.get(1.0, "end-1c")
    }

    TextureConverter.TextureConverter()

def SetAppWindowProperties(app):
    app.title("TextureConverterPY")
    app.geometry("420x180")
    app.resizable(False,False)
    app.iconbitmap(os.path.abspath("Resources/icon.ico"))
    return app

# Main part of this file is configuring window, and running it
app = customtkinter.CTk()
app = SetAppWindowProperties(app)

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady = 0, padx=0, fill="both", expand=True)

labelSetting = customtkinter.CTkLabel(master=frame, text="Please set the original extension, after set edited extension, and path")
labelSetting.pack(pady=2, padx=10)

frameTextBoxes = customtkinter.CTkFrame(master=frame)
frameTextBoxes.pack(pady = 0, padx=0, fill="both")

textBoxOriginal = customtkinter.CTkTextbox(master=frameTextBoxes, height=20, border_spacing=1, border_width=1, corner_radius=1)
textBoxOriginal.pack(pady=2, padx=10, fill="both")

textBoxEdited = customtkinter.CTkTextbox(master=frameTextBoxes, height=20, border_spacing=1, border_width=1, corner_radius=1)
textBoxEdited.pack(pady=2, padx=10, fill="both")

textBoxPath = customtkinter.CTkTextbox(master=frameTextBoxes, height=20, border_spacing=1, border_width=1, corner_radius=1)
textBoxPath.pack(pady=2, padx=10, fill="both")

isTexCheckBox = customtkinter.CTkCheckBox(master=frame, text="Is generating tex files")
isTexCheckBox.pack(pady=2, padx=10)

runButton = customtkinter.CTkButton(master=frame, text="Convert Textures", width=420, height=30, command=TextureConverterExec)
runButton.pack(side="top", pady=3, padx=2)

app.mainloop()
