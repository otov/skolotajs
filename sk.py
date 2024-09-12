class Skolotajs:
    def __init__(self, skaits, tips, klase):
        self.skaits = skaits
        self.tips = tips
        self.klase = klase
        self.tips = None
class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards1):
        self.uzvards1= uzvards1
        self.tips = 1
    def izvade1(self):
        print(
            "Sākumskolas (tips-{}) Skolotajs {} māca {} stundas {} klasē."
            ).format(self.tips, self.uzvards1, self.skaits, self.klase)

class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards2, pirmais, otrais, kopsk):
        self.uzvards2=uzvards2
        self.pirmais= pirmais
        self.otrais= otrais
        self.kopsk=kopsk
        self.tips=3
    def izvade2(self):
        print(
            "Vidusskolas (tips-{}) skolotājs {} māca šādus priekšmetus: {} un {}, kopā {} stundas."
         ).format(self.tips, self.uzvards2, self.pirmais, self.otrais, self.kopsk)


uzvards1=input("Ievadiet sākumskolas skolotāja uzvārdu: ")
klase=input("Ievadiet klasi: ")
skaits=input("Ievadiet skolotāja stundu skaitu: ")

#uzvards2=input("Ievadiet vidusskolas skolotāja uzvārdu: ")
#pirmais=input("Ievadiet pirmo pasniegto priekšmetu: ")
#skaits1=int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
#otrais=input("Ievadiet otro pasniegto priekšmetu: ")
#skaits2=int(input("Ievadiet otrā priekšmeta stundu skaitu: "))



object1=SakumskolasSkolotajs(tips,uzvards1,skaits,klase)
print(object1.izvade1())
object1.izvade1()




         

