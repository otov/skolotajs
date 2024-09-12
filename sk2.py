class Skolotajs:
    def __init__(self, skaits, tips):
        self.skaits = skaits
        self.tips = tips
        self.tips = tips
class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards1, klase):
        self.uzvards1= uzvards1
        self.klase = klase
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
    def izvade2(self):
        print(
            "Vidusskolas (tips-{}) skolotājs {} māca šādus priekšmetus: {} un {}, kopā {} stundas."
         ).format(self.tips, self.uzvards2, self.pirmais, self.otrais, self.kopsk)


tips=int(input("Ievadiet skolotāja tipu (Pamatskolas skolotājs: 1   Vidusskolas skolotajs: 3): "))
if tips == 1:
    uzvards1=input("Ievadiet sākumskolas skolotāja uzvārdu: ")
    klase=input("Ievadiet klasi: ")
    skaits=input("Ievadiet skolotāja stundu skaitu: ")

    object1=SakumskolasSkolotajs(tips,uzvards1,skaits,klase)
    print(object1.izvade1())
    object1.izvade1()

elif tips == 3:
    uzvards2=input("Ievadiet vidusskolas skolotāja uzvārdu: ")
    pirmais=input("Ievadiet pirmo pasniegto priekšmetu: ")
    skaits1=int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
    otrais=input("Ievadiet otro pasniegto priekšmetu: ")
    skaits2=int(input("Ievadiet otrā priekšmeta stundu skaitu: "))
    

    kopsk=skaits1+skaits2

    object2=VidusskolasSkolotajs(tips,uzvards2,pirmais,otrais,kopsk)
    print(object2.izvade2())
    object2.izvade2()
else:
    print("Ievadīts nederīgs tips!")