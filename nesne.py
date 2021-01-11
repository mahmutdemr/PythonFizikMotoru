# from _typeshed import SupportsGetItem
from tkinter import Canvas
from rigid import Rigid
from sabitler import WIDTH, HEIGHT, genislik
import random
from Vector import Vector2


class Nesne:

    birimGenislik = 50

    def __init__(self, isim, rigid, sprite, scale):
        
        renkler = ['#ffa670', '#fffc97', '#ff5150', '#e500f0', '#2cff06', '#af7100', '#0d00bd', '#aaffdc']
        self.renk = random.choice(renkler)
        
        self.isim = isim
        self.rigid = rigid
        self.konum = rigid.konum 
        self.sprite = sprite
        self.scale = scale * 25
        self.eskiKonum = rigid.konum
        # self.rigid.collider.scale = self.scale

        self.rigid.collider.BoyutAta(self.scale)
        self.rigid.isim = isim
        Rigid.tumRigidler.append(self.rigid)
        self.goruntu = self.sprite.Cizdir(self.rigid.konum, self.rigid.collider.scale, self.renk)

    def Guncelle(self):
        
        self.rigid.FizikselHesap()
        self.konum = self.rigid.Konum()

    def Cizdir(self):
        self.goruntu = self.sprite.Cizdir(self.rigid.konum, self.rigid.collider.scale, self.renk)
        # Nesne.canvas.create_oval(self.konum.x - genislik / 2, self.konum.y - genislik / 2, self.konum.x + genislik / 2, self.konum.y + genislik / 2, fill= self.renk)
    
    def Tasi(self):
        self.sprite.Tasi(self.rigid.konum - self.scale)
        self.eskiKonum = self.rigid.konum

    def Sildir(self):
        self.sprite.Sildir()
