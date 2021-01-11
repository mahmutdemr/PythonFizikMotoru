from simulasyon import Simulasyon
from sabitler import WIDTH, HEIGHT
from Vector import Vector2
from tkinter import *

master = Tk()

w = Canvas(master, width=WIDTH, height=HEIGHT)

def callback(event):
    SimulasyonYonetici.SabitBirimKure(Vector2(event.x, event.y))

w.bind("<Button-1>", callback)

x = Canvas(master, width=WIDTH, height=50, background="#aaffff")
z = Scale(master, from_=0, to=50, orient=HORIZONTAL)

z.pack()
z.set(0)
w.pack()    
x.pack()

SimulasyonYonetici = Simulasyon(w, x, z)
islem = SimulasyonYonetici.StartSim()

def on_closing():
    SimulasyonYonetici.SimDurdur()
    master.destroy()

master.protocol("WM_DELETE_WINDOW", on_closing)
master.mainloop()


