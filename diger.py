from Vector import Vector2
# from nesne import Nesne
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
        # self.size = size
        self.scale = Vector2(1,1)

    def BoyutAta(self, boyut):
        self.scale = boyut

class KureSprite:
    def __init__(self):
        self.goruntu = KureSprite.canvas.create_oval(0, 0, 0, 0, fill="white")

    def Cizdir(self, merkez, buyukluk, renk):
        self.goruntu = KureSprite.canvas.create_oval(merkez.x - buyukluk.x, merkez.y - buyukluk.y, merkez.x + buyukluk.x, merkez.y + buyukluk.y, fill = renk)

    def Tasi(self, miktar):
        KureSprite.canvas.moveto(self.goruntu, miktar.x, miktar.y)
    def Sildir(self):
        KureSprite.canvas.delete(self.goruntu)


class KareSprite:
    def __init__(self):
        self.goruntu = KureSprite.canvas.create_rectangle(0, 0, 0, 0, fill="white")

    def Cizdir(self, merkez, buyukluk, renk):
        self.goruntu = KureSprite.canvas.create_rectangle(merkez.x - buyukluk.x, merkez.y - buyukluk.y, merkez.x + buyukluk.x, merkez.y + buyukluk.y, fill = renk)

    def Tasi(self, miktar):
        KureSprite.canvas.moveto(self.goruntu, miktar.x, miktar.y)

    def Sildir(self):
        KureSprite.canvas.delete(self.goruntu)


