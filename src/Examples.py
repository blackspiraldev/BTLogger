'''
Created on Dec 12, 2010

@author: jatapper
'''
from Tkinter import *
root = Tk()
# define rows and columns that should expand on window resizing
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
Label(root, text='Label1', bg='white').grid(row=0, column=0, sticky='ew')
Label(root, text='Label2', bg='yellow').grid(row=0, column=1)
Label(root, text='Label3', bg='green').grid(row=0, column=2)
Label(root, text='Label4', bg='red').grid(row=1, column=0, columnspan=2, sticky='nsew')
Label(root, text='Label5', bg='blue').grid(row=2, column=0, columnspan=3, sticky='nsew')
root.mainloop()