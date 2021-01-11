from Vector import Vector2
from tkinter import Canvas

class SphereCollider:
    def __init__(self, offset, radius):
        self.tur = 0
        self.offset = offset
        self.radius = radius
        self.scale = Vector2(1, 1)

    def BoyutAta(self, boyut):
        self.scale = boyut

class BoxCollider:
    def __init__(self, offset):
        self.tur = 1
        self.offset = offset
        self.scale = Vector2(1,1)

    def BoyutAta(self, boyut):
        self.scale = boyut

class KureSprite:
    def Cizdir(self, merkez, buyukluk, renk):
        self.goruntu = KureSprite.canvas.create_oval(merkez.x - buyukluk.x, merkez.y - buyukluk.y, merkez.x + buyukluk.x, merkez.y + buyukluk.y, fill = renk)

    def Tasi(self, miktar):
        KureSprite.canvas.moveto(self.goruntu, miktar.x, miktar.y)


class KareSprite:
    def Cizdir(self, merkez, buyukluk, renk):
        self.goruntu = KureSprite.canvas.create_rectangle(merkez.x - buyukluk.x, merkez.y - buyukluk.y, merkez.x + buyukluk.x, merkez.y + buyukluk.y, fill = "black")

    def Tasi(self, miktar):
        KureSprite.canvas.moveto(self.goruntu, miktar.x, miktar.y)


