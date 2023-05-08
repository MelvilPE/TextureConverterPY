from __future__ import annotations

import os
import sys

from cx_Freeze import Executable, setup
SCRIPT_NAME = "Main.py"

base = "Win32GUI" if sys.platform == "win32" else None
executable = [Executable(SCRIPT_NAME, base=base)]
includeFiles = [
    "Resources"
]

setup(
    name = "TextureConverterPY",
    version = "1.0.0",
    description = "ResourceEditor Plugin",
    options = {
        "build_exe": {
            "include_files": includeFiles
        }
    },

    executables=executable,
)