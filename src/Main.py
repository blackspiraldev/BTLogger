'''
Created on Dec 12, 2010

@author: jatapper

Simple GUI script/app to follow tails and allow graphical grep/re checking.

Limitation: This wont work accross multiple lines in this version.
Could be fairly easily worked around possibly.

Aims for this app.

1. Simple 'baretail' like support for x-platform
2. Quick regex checker (but will currently be limited to 'lines' mode)

Cfg options (regex --> colour mappings stored in configuration file (ini style))


To Consider adding:

1. Live regex testing on text entry. This shouldnt be too hard to implement.
2. Loading the file in open dialog and via a path
3. 'Follow' suppport ala tail -f

'''
from Tkinter import *
import re
import ConfigParser

def getconfig():
    config = ConfigParser.RawConfigParser()
    config.read('settings.cfg')
    sections = config.sections()
    l = []
    for s in sections:
        l.append((config.get(s, "bg"),
                 config.get(s, "fg"),
                 config.get(s, "regex")))
        
    return l

def applyFilter(listbox, configs, line):
    for c in configs:
        new_pattern = re.compile(c[2], re.IGNORECASE)
        matches = new_pattern.findall(line)
        if matches:
            s = listbox.size() - 1
            listbox.itemconfigure(s, fg = c[1], bg = c[0] )

class FilterableListbox(Listbox):
    '''
    This listbox should now be able to become 'filtered' based
    on results of a RE.
    
    Not yet thought of a sensible way to store the history..
    '''

    
    def applyfilter(self, regex, config):
        
        if len(regex) < 1:
            self.delete(0, self.size()-1)
            if self.original_list:
                for l in self.original_list:
                    self.insert(END, l)
                    applyFilter(self, config, l)
            return
        
        new_pattern = re.compile(regex, re.IGNORECASE)
        new_list = []
        for l in range(0, self.size()-1):
            matches = new_pattern.findall(self.get(l))
            if matches:
                new_list.append(self.get(l))
                
        if len(new_list) > 0:
            try:
                if len(self.original_list) < 1:
                    self.original_list = self.get(0, self.size() -1)
            except:
                self.original_list = self.get(0, self.size() -1)
            
             
                           
            self.delete(0, self.size())
            for l in new_list:
                self.insert(END, l)    
                applyFilter(self, config, l)
        
class App:
    
    def __init__(self, master):
        self.config = getconfig()
        
        master.grid_rowconfigure(1, weight=1)
        master.grid_rowconfigure(2, weight=1)
        master.grid_rowconfigure(3, weight=1)
        master.grid_columnconfigure(0, weight=1)
        
#        frame = Frame(master)
#        frame.pack()

        self.button = Button(master, text="QUIT", fg="red", command=master.quit)
        self.button.grid(row=0,column=0, sticky='ew')
#        self.button.pack(side=LEFT)

        #Two list boxes are required 1 for the unfiltered view
        #and one for the filtered view
        self.fullviewSB = Scrollbar(master, orient=VERTICAL)
        self.fullview = Listbox(master, yscrollcommand=self.fullviewSB.set)
        self.fullviewSB.config(command=self.fullview.yview)
#        self.fullviewSB.pack(side=RIGHT, fill=Y)
        self.fullview.grid(row=1, column=0, columnspan='3', sticky='nsew')
        
        
#        self.fullview.pack()
        
        #Add the filter text box plus a button
        self.filterentry = Entry(master)
        self.filterentry.grid(row=2, column=0,columnspan='2', sticky='nsew')
#        self.filterentry.pack()
        
        self.filterbutton = Button(master, text="Filter", command=self.filter)
        self.filterbutton.grid(row=2,column=3, sticky='ns')

        self.filteredview = Listbox(master)
        self.filteredview.grid(row=3, column=0, columnspan='3', sticky='nsew')
        
        self.testview = FilterableListbox(master)
        self.testview.grid(row=4,column=0,columnspan='3', sticky='nsew')
        
        
        self.insert_dummy()
        
    
    def filter(self):
        
        #Try out the new filterable view
        self.testview.applyfilter(self.filterentry.get(), self.config)
        
        self.filteredview.delete(0, self.filteredview.size())
        #self.filteredview.insert(END, self.filterentry.get())
        new_pattern = re.compile(self.filterentry.get(), re.IGNORECASE)
        for l in range(0, self.fullview.size()-1):
            matches = new_pattern.findall(self.fullview.get(l))
            if matches:
                self.filteredview.insert(END, self.fullview.get(l))
                applyFilter(self.filteredview, self.config, self.fullview.get(l))
    
    def insert_dummy(self):
        self.fullview.insert(END, "This is a test entry to see")
        self.testview.insert(END, "This is a test entry to see")
        applyFilter(self.fullview, self.config, "This is a test entry to see")
        
        for x in range(0,200):
            self.fullview.insert(END, str(x))
            applyFilter(self.fullview, self.config, str(x))
            self.testview.insert(END, str(x))
        
    def insert(self):
        self.fullview.insert(END, "test")        
        self.fullview.itemconfigure(self.fullview.size() - 1, bg="blue", fg="red")

if __name__ == '__main__':
    
    master = Tk()
    app = App(master)
    
    master.mainloop()