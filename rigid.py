from zaman import Zaman
from Vector import Vector2
import sabitler
from diger import SphereCollider, BoxCollider
import random

class Rigid:
    
    tumRigidler = []
    rigidIdleri = []

    def __init__(self, nesneHiz, nesneAgirlik, konum, isKinematic, collider):
        self.hiz = nesneHiz
        self.konum = konum
        self.agirlik = nesneAgirlik
        self.isKinematic = isKinematic
        self.collider = collider
        self.temasEdenler = []

        id = random.randint(0, 1000)
        while id in Rigid.rigidIdleri:
            id = random.randint(0, 1000)
        Rigid.rigidIdleri.append(id)
        self.id = id
    
    def Degerler(self):
        return "hiz:" + str(round(self.hiz.x)) + " Agirlik:" + str(round(self.agirlik)) + " Momentum:" + str(round(self.Momentum())) + ""

    def Momentum(self):
        return (self.hiz.length() * self.agirlik)

    def BilgiAl(self):
        array = [self.hiz, self.agirlik]
        return array
    
    def HizAta(self, nesneHiz):
        self.hiz = nesneHiz
    
    def FizikselHesap(self):
        self.konum += self.hiz * Zaman.deltaZaman * 10 * sabitler.hizScale

    def Konum(self):
        return self.konum
