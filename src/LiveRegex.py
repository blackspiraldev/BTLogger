'''
Created on Dec 12, 2010

@author: jatapper
'''

from Tkinter import *
import re


class App:
    
    def __init__(self, master):
        
        self.textview = Text(master)
        self.textview.grid(row=0, column=0)
        
        self.entryfield = Entry(master)
        self.entryfield.grid(row=1,column=0)
        
        self.button = Button(master, text="Search", command=self.search)
        self.button.grid(row=2, column=0)
        
        self.textview.insert(INSERT, open("/Users/jatapper/Documents/workspace/affiliatetools-hg/tests/charley-chase.html").read())
        
    def search(self):
        t = self.textview.search(self.entryfield.get(), ,regexp=True)
        print t



if __name__ == '__main__':
    
    
    master = Tk()
    master.geometry('600x600-5+40')
    app = App(master)
    
    
    master.mainloop()