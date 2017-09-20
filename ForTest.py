
import os
import tkinter.filedialog

filename = tkinter.filedialog.askopenfile()
print(filename.name)
print(os.path._getfullpathname(filename.name))