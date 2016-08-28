import tkinter as tk

Material = ["PET","HDPE","MP"]
Comp = [.5,.25,.25] # Adds to 1
Baler1 = [50,25,50] # Processing Capability in Tons Per Hour
Bunker = [100,100,100] # Capacity in Tons
TPH = 35
InitialFill = [0,0,0]
Shift = 8 #hours

Fill = [InitialFill]
current = [0,0,0]
last = [0,0,0]

for x in range(0, Shift):
    for y in range(0, len(Comp)):
        current[y] = last[y] + Comp[y]*TPH
    Fill.append(list(current))
    last = list(current)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="left")

        self.quit = tk.Button(self, text = "QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="left")



    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
