from rigid import Rigid
import random

class Nesne:
    birimGenislik = 25

    def __init__(self, isim, rigid, sprite, scale):
        renkler = ['#ffa670', '#fffc97', '#ff5150', '#e500f0', '#2cff06', '#af7100', '#0d00bd', '#aaffdc']
        self.renk = random.choice(renkler)
        
        self.isim = isim
        self.rigid = rigid
        self.konum = rigid.konum 
        self.sprite = sprite
        self.scale = scale * Nesne.birimGenislik

        self.rigid.collider.BoyutAta(self.scale)
        self.rigid.isim = isim
        Rigid.tumRigidler.append(self.rigid)
        self.goruntu = self.sprite.Cizdir(self.rigid.konum, self.rigid.collider.scale, self.renk)

    def Guncelle(self):
        self.rigid.FizikselHesap()
        self.konum = self.rigid.Konum()

    def Cizdir(self):
        self.goruntu = self.sprite.Cizdir(self.rigid.konum, self.rigid.collider.scale, self.renk)
    
    def Tasi(self):
        self.sprite.Tasi(self.rigid.konum - self.scale)

