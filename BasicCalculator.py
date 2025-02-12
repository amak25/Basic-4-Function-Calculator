from tkinter import *
 
#Preconfigured frame for calculator GUI
def CalcFrame(source, side):
    storeObj = Frame(source, borderwidth=8, bd=8, bg="IndianRed1")
    storeObj.pack(side=side, expand =YES, fill =BOTH)
    return storeObj

#Preconfigured framework for button
def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand = YES, fill=BOTH)
    return storeObj

#GUI and functions for Calculator
class app(Frame):
    def __init__(self):  #
        Frame.__init__(self)
        self.option_add('*Font', 'Ubuntu 20 bold')
        self.pack(expand = YES, fill =BOTH)
        self.master.title('Calculator')
        
        display = StringVar() 
        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=30, bg="IndianRed1").pack(side=TOP, expand=YES, fill=BOTH) #Window to allow for user input and display it
    
        for clearButton in (["C"]): #Clear Button 
            erase = CalcFrame(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set('')) #Clears display
        
        for numButton in ("789/", "456*", "123-", "0.>+"): #Numbers and operators
            FunctionNum = CalcFrame(self, TOP)
            for iEquals in numButton:
                if iEquals == ">": #Backspace Button
                    button(FunctionNum, LEFT, iEquals, lambda storeObj=display, q=iEquals: storeObj.set(storeObj.get() [:-1])) #Removes one character from the display
                else:
                    button(FunctionNum, LEFT, iEquals, lambda storeObj=display, q=iEquals: storeObj.set(storeObj.get() + q)) #Adds selected Character to display
            
        EqualButton = CalcFrame(self,TOP)
        for iEquals in "=": # Equal button
            if iEquals == '=':
                buttonEquals = button(EqualButton, LEFT, iEquals)
                buttonEquals.bind('<ButtonRelease-1>', lambda e, s=self, storeObj=display: s.calc(storeObj), '+') #Processes data stored in display or storeObj Variable

            else:
                buttonEquals = button(EqualButton, LEFT, iEquals, lambda storeObj=display, s='%s' % iEquals: storeObj.set(storeObj.get() + s))
                
    def calc(self, display):
        try:
            display.set(eval(display.get())) #Displays processed input
        except:
            display.set("ERROR") #Gives error message if input failed to be processed
            

#Runs Calculator
if __name__=='__main__':
    app().mainloop()
    

