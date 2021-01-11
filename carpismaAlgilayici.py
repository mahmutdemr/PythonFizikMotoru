from rigid import Rigid
from Vector import Vector2
import math

class Carpisma:

    tumNesneler = []
    tumDuvarlar = []
    points = []
    nesneSayisi = 0
    duvarSayisi = 0
    carpismaSayisi = 0

    @staticmethod
    def NesneEkle(nesne):
        Carpisma.tumNesneler.append(nesne)
        Carpisma.nesneSayisi += 1

    @staticmethod
    def DuvarEkle(duvar):
        Carpisma.tumDuvarlar.append(duvar)
        Carpisma.duvarSayisi += 1

    @staticmethod
    def CarpismaHesapla():

        tumRigidler = Rigid.tumRigidler

        for i in range(Carpisma.nesneSayisi):
            for j in range(i + 1 , Carpisma.nesneSayisi):
                cikti = Carpisma.CarpisiyorMu(tumRigidler[i], tumRigidler[j])
                if cikti[0]:
                    
                    if tumRigidler[j].id not in tumRigidler[i].temasEdenler:
                        
                        tumRigidler[j].temasEdenler.append(tumRigidler[i].id)
                        tumRigidler[i].temasEdenler.append(tumRigidler[j].id)
                        Carpisma.Carpistir(tumRigidler[j], tumRigidler[i], cikti[1])
                    
                    else:
                        pass
                
                else:
                    if tumRigidler[i].id in tumRigidler[j].temasEdenler:
                        
                        tumRigidler[j].temasEdenler.remove(tumRigidler[i].id)
                        tumRigidler[i].temasEdenler.remove(tumRigidler[j].id)


        


    @staticmethod
    def Carpistir(sol, sag, carpismaNoktasi):
        Carpisma.carpismaSayisi += 1

        if sol.isKinematic and sag.isKinematic:
            return
        elif not sol.isKinematic and not sag.isKinematic:
            Carpisma.EsnekCarpisma(sol, sag)
        elif sol.isKinematic:
            Carpisma.DinamikVeKinematik(sol, sag, carpismaNoktasi)
        else:
            Carpisma.DinamikVeKinematik(sag, sol, carpismaNoktasi)


    @staticmethod
    def EsnekCarpisma(sol, sag):
        bilgi1 = sol.BilgiAl()
        bilgi2 = sag.BilgiAl()

        v1 = bilgi1[0]
        v2 = bilgi2[0]

        m1 = bilgi1[1]
        m2 = bilgi2[1]

        sol.HizAta(Carpisma.TamVektorHizHesap(v1,v2,m1,m2,sol.konum, sag.konum))
        sag.HizAta(Carpisma.TamVektorHizHesap(v2,v1,m2,m1,sag.konum, sol.konum))

    @staticmethod
    def DinamikVeKinematik(sabit, hareketli, point):
        Carpisma.points.append(point)
        hiz = hareketli.BilgiAl()[0]

        if abs(point.y - hareketli.konum.y) < abs(point.x - hareketli.konum.x):
            hareketli.HizAta(Vector2(-1 * hiz.x, hiz.y))
        else:
            hareketli.HizAta(Vector2(hiz.x, -1 * hiz.y))
    
    @staticmethod
    def CarpisiyorMu(rigid1, rigid2):
        
        if(rigid1.collider.tur == 0 and rigid2.collider.tur == 0):
            return Carpisma.SpheretoSphere(rigid1, rigid2)

        elif(rigid1.collider.tur == 1 and rigid2.collider.tur == 1):
            return Carpisma.BoxtoBox(rigid1, rigid2)

        else:
            return Carpisma.BoxtoSphere(rigid1, rigid2)
        
    
    @staticmethod
    def BoxtoBox(collider1, collider2):
        
        return [False, False]

        yatayUzaklik = collider1.collider.size.x + collider2.collider.size.x
        yataySonuc = abs(collider1.konum.x - collider2.konum.x) < yatayUzaklik

        dikeyUzaklik = collider1.collider.size.y + collider2.collider.size.y
        dikeySonuc = abs(collider1.konum.y - collider2.konum.y) < dikeyUzaklik
        
        return yataySonuc and dikeySonuc

    @staticmethod
    def SpheretoSphere(collider1, collider2):
        cap = collider1.collider.radius + collider2.collider.radius

        if (collider1.konum - collider2.konum).length() <= cap:
            return [True, True]
        else:
            return [False, False]
        

    @staticmethod
    def BoxtoSphere(collider1, collider2):
        kutu = collider1
        kure = collider2
        if(kutu.collider.tur == 0):
            var1 = kutu
            kutu = kure
            kure = var1

        sagUst = kutu.konum + kutu.collider.scale
        solAlt = kutu.konum - kutu.collider.scale

        x = max(solAlt.x, min(kure.konum.x, sagUst.x));
        y = max(solAlt.y, min(kure.konum.y, sagUst.y))

        distance = math.sqrt((x - kure.konum.x) * (x - kure.konum.x) + (y - kure.konum.y) * (y - kure.konum.y))
        sonuclar = [distance <= kure.collider.radius, Vector2(x, y)]
        
        return sonuclar
            

    @staticmethod
    def TamVektorHizHesap(v1, v2, m1, m2, x1, x2):
        var1 = 2 * m2 / (m1 + m2)
        var2 = Carpisma.IcCarpim(v1 - v2, (x1 - x2).normalized())
        var3 = x1 - x2

        var4 = var1 * var2 / var3.length()
        var5 = Vector2(var4 * var3.x, var4 * var3.y)

        sonuc = v1 - var5
        
        return sonuc

    @staticmethod
    def IcCarpim(vek1, vek2):
        return vek1.x * vek2.x + vek1.y * vek2.y
