from tkinter import *
from interface.canvas import *
from interface.configuration import *

mainwidonws = Tk()

config = Configuration(mainwidonws)
config.grid(row=0, column=0, sticky=W)
canvas = Space(mainwidonws)  # ,background="black")

canvas.addParticle(100, 10,  5.972e15, 20)
canvas.addParticle(200, 10,  5.972e15, 20)
canvas.addParticle(200, 200, 5.972e15, 20)

canvas.grid(row=0, column=1, sticky=E)

while (True): #équivaleur de mainloop mais personalisé
	try:
		canvas.update()
		mainwidonws.update()
	except Exception as e:
		print("exit")
		break
	

