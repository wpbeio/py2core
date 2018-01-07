#!/usr/bin/env python
from functools import partial
import tkinter

root = tkinter.Tk()
Mybutton = partial(tkinter.Button, root, fg='white', bg='red')
b1 = Mybutton(text='button1')
b2 = Mybutton(text='button2')
qb = Mybutton(text='QUIT', bg='blue', command=root.quit)
b1.pack()
b2.pack()
qb.pack(fill=tkinter.X, expand=True)
root.title('testPFAs!')
root.mainloop()
