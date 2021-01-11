from sabitler import HEIGHT, genislik
class Duvar:

    def __init__(self, ctx , isim , duvarKonum):
        self.isim = isim
        self.renk = '#000000'
        self.ctx = ctx
        self.konum = duvarKonum
        self.temasEdenler = ["deneme" , "string"]
    
    def Cizdir(self):
        self.ctx.create_rectangle(self.konum.x - genislik / 2, self.konum.y - genislik / 2, self.konum.x + genislik / 2, self.konum.y + genislik / 2, fill="black")
