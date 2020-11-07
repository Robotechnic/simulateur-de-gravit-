from tkinter import *
from interface.canvas import *
from interface.configuration import *

from modules.vector import *
from modules.objects import *

mainwidonws = Tk()

config = Configuration(mainwidonws)
config.grid(row=0,column=0,sticky=W)
canvas = Space(mainwidonws)#,background="black")

canvas.addParticle(100,100,1,20)
canvas.addParticle(200,10,45,20)

canvas.grid(row=0,column=1,sticky=E)

mainwidonws.after(100,canvas.update)
mainwidonws.mainloop()