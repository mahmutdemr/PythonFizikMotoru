from datetime import datetime
import threading

class Zaman:
    deltaZaman = (datetime.now() - datetime.now()).total_seconds()
    def __init__(self):
        self.oncekiZaman = datetime.now()
        self.anlinZaman = datetime.now()
        self.deltaZaman = (datetime.now() - datetime.now()).total_seconds()

    def Guncelle(self):
        self.anlikZaman = datetime.now()
        self.deltaZaman = (self.anlikZaman - self.oncekiZaman).total_seconds()
        self.oncekiZaman = self.anlikZaman
        Zaman.deltaZaman = self.deltaZaman

    def Delta(self):
        return self.deltaZaman

    def SetInterval(self, func, sec):
        def func_wrapper():
            func()
            self.SetInterval(func, sec)

        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t

    def Yazdir(self):
        print("Deneme")
