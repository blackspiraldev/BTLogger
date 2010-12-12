'''
Created on Dec 12, 2010

@author: jatapper
'''
from Tkinter import *
import re

class App:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        
        #Two list boxes are required 1 for the unfiltered view
        #and one for the filtered view
        self.fullview = Listbox(master)
        self.fullview.pack()
        
        #Add the filter text box plus a button
        self.filterentry = Entry(master, width="50")
        self.filterentry.pack()
        
        self.filterbutton = Button(master, text="Filter", command=self.filter)
        self.filterbutton.pack(side=LEFT)        
#        self.fullview.insert(END, "Top of the list")
#        self.fullview.insert(END, "Bottom of the list")
        self.filteredview = Listbox(master)
        self.filteredview.pack()
        
        self.insert_dummy()
    
    def filter(self):
        self.filteredview.delete(0, self.filteredview.size())
        #self.filteredview.insert(END, self.filterentry.get())
        new_pattern = re.compile(self.filterentry.get(), re.IGNORECASE)
        for l in range(0, self.fullview.size()-1):
            matches = new_pattern.findall(self.fullview.get(l))
            if matches:
                self.filteredview.insert(END, self.fullview.get(l))
    
    
    def insert_dummy(self):
        self.fullview.insert(END, "This is a test entry to see")
        
        for x in range(0,200):
            self.fullview.insert(END, str(x))
        
        
    def insert(self):
        self.fullview.insert(END, "test")        
        self.fullview.itemconfigure(self.fullview.size() - 1, bg="blue", fg="red")

if __name__ == '__main__':
    
    master = Tk()
    app = App(master)
    
    master.mainloop()