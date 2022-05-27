from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

root = Tk()
app = Window(root)

root.geometry("400x400")
root.attributes('-alpha', 0.5) # Not transparent enough
root.wm_title("Virtual Assistant")
root.mainloop()
