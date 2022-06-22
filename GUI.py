from calendar import calendar
from tkinter import *

# Calender icon from Freepik

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

root = Tk()
app = Window(root)

root.geometry("1200x800")
root.wait_visibility(root)
root.wm_title("Virtual Assistant")
root.resizable(False, False)
root['bg'] = '#0a0a0a'

# Calender Button Frame

calBtnFrame = Frame(root)
calBtnFrame.pack()

def setWindow():
    print('clicked')

calenderIcon = PhotoImage(file = 'Images\calendar.png')
    
calenderBtn = Button(calBtnFrame, image = calenderIcon, command = setWindow, bg = '#0a0a0a', highlightthickness = 0, bd = 0)
calenderBtn.pack()

root.mainloop()