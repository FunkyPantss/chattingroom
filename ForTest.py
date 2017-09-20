#
# from tkinter import *
#
#
# root = Tk()
#
# textpad = Text(root)
# label = Label(root)
# label.pack()
# textpad.pack()
#
# mark = 'mark'
#
# textpad.mark_set(mark, CURRENT + ' lineend')
# textpad.insert(mark, 'asdasdasd')
# #textpad.insert(SEL_LAST, 'adsdasd')
# #textpad.config(state=DISABLED)
# import time
# print(time.ctime())
#
#
#
#
# textpad.insert(END, 'hello\n')
# textpad.insert(END, 'world')
# textpad.insert(mark, '1111111')
# # textpad.pack_forget()
# # textpad.pack()
#
#
# root.mainloop()

import os
import tkinter.filedialog

filename = tkinter.filedialog.askopenfile()
print(filename.name)
print(os.path._getfullpathname(filename))