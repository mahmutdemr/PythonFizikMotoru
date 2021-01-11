from zaman import Zaman
from nesne import Nesne
from carpismaAlgilayici import Carpisma
from sabitler import WIDTH, HEIGHT , fizikFps, goruntuFps , genislik
import sabitler
from Vector import Vector2
from diger import SphereCollider, BoxCollider, KareSprite, KureSprite
from rigid import Rigid

class Simulasyon:
    def __init__(self, ctx, bilgi, slider):
        self.zamanRef = Zaman()
        self.ctx = ctx
        self.bilgi = bilgi
        self.nesneler = []
        self.slider = slider        
        KureSprite.canvas = self.ctx


    def StartSim(self):

        rigid1 = Rigid(Vector2(0,0), 1, Vector2(WIDTH / 2, genislik / 2), True, BoxCollider(Vector2(0, 0)))
        self.NesneUret("Duvar1", rigid1, KareSprite(), Vector2(WIDTH / 50 - 2, 1))
        
        rigid2 = Rigid(Vector2(0,0), 1, Vector2(WIDTH / 2, HEIGHT - genislik / 2), True, BoxCollider(Vector2(0, 0)))
        self.NesneUret("Duvar2", rigid2, KareSprite(), Vector2(WIDTH / 50 - 2, 1))
        rigid3 = Rigid(Vector2(0, 0), 1, Vector2(genislik / 2,HEIGHT / 2), True, BoxCollider(Vector2(0, 0)))
        self.NesneUret("Duvar3", rigid3, KareSprite(), Vector2(1, (HEIGHT / 50) - 2))
        rigid4 = Rigid(Vector2(0,0), 1, Vector2(WIDTH - genislik / 2, HEIGHT / 2), True, BoxCollider(Vector2(0, 0)))
        self.NesneUret("Duvar4", rigid4, KareSprite(), Vector2(1, (HEIGHT / 50) - 2))

        rigid1 = Rigid(Vector2(5, 3), 100, Vector2(100, 100), False, SphereCollider(Vector2(0, 0), 25 * 1.5))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1.5, 1.5))

        rigid1 = Rigid(Vector2(3,5), 1, Vector2(200, 200), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        rigid1 = Rigid(Vector2(0,0), 1, Vector2(300, 100), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        rigid1 = Rigid(Vector2(0,0), 1, Vector2(400, 200), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        rigid1 = Rigid(Vector2(0,0), 1, Vector2(500, 100), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        rigid1 = Rigid(Vector2(0,0), 1, Vector2(600, 200), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        rigid1 = Rigid(Vector2(0,0), 1, Vector2(700, 100), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        rigid1 = Rigid(Vector2(0,0), 1, Vector2(800, 200), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        rigid1 = Rigid(Vector2(0,0), 1, Vector2(900, 100), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        rigid1 = Rigid(Vector2(0,0), 1, Vector2(300, 300), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        rigid1 = Rigid(Vector2(0,0), 1, Vector2(400, 400), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        rigid1 = Rigid(Vector2(0,0), 1, Vector2(500, 300), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        rigid1 = Rigid(Vector2(0,0), 1, Vector2(600, 400), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        rigid1 = Rigid(Vector2(0,0), 1, Vector2(700, 300), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        rigid1 = Rigid(Vector2(0,0), 1, Vector2(800, 400), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        rigid1 = Rigid(Vector2(0,0), 1, Vector2(900, 300), False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))


        Carpisma.tumNesneler = self.nesneler
        Carpisma.nesneSayisi = len(self.nesneler)

        self.sim = True
        self.dongu = self.zamanRef.SetInterval(self.SimDongu, 1/goruntuFps)
        self.FizikDongu = self.zamanRef.SetInterval(self.FizikHesaplari, 1/fizikFps)

        return self.dongu

    def SabitBirimKure(self, konum):
        rigid1 = Rigid(Vector2(0,0), 1, konum, False, SphereCollider(Vector2(0, 0), 25))
        self.NesneUret("nesne1", rigid1, KureSprite(), Vector2(1, 1))
        Carpisma.tumNesneler = self.nesneler
        Carpisma.nesneSayisi = len(self.nesneler)

    def NesneUret(self, isim, rigid1, sprite, scale):
        self.nesneler.append(Nesne(isim, rigid1, sprite, scale))


    def SimDurdur(self):
        self.dongu.cancel()
        self.FizikDongu.cancel()

        self.sim = False

    def SimDongu(self):
        self.Cizdir()

    def FizikHesaplari(self):
        if self.sim :
            sabitler.hizScale = self.slider.get() / 10
            self.zamanRef.Guncelle()
            Carpisma.CarpismaHesapla()
            self.Guncelle()

    def Guncelle(self):
        for i in self.nesneler:
            i.Guncelle()

    def Cizdir(self):
        self.bilgi.delete("all")
        j = 0
        momentum = 0
        for i in self.nesneler:
            i.Tasi()
            # self.bilgi.create_text(150, 10 + 15 * j, text= str(j + 1)+ ". : " + i.rigid.Degerler())
            # momentum += i.rigid.hiz.x * i.rigid.agirlik
            # j += 1

        # self.bilgi.create_text(150, 10 + 15 * j, text="Carpisma : " + str(Carpisma.carpismaSayisi) + "  Momentum : " + str(momentum))


