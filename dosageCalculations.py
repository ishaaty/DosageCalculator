
#def kgs_check(weight):
        #if "kgs" in weight:
            #w = weight.split(" ")
            #kgs = float(w[0])
        #else:
            #w = weight.split(" ")
            #lbs = float(w[0])
            #kgs = float(f"{lbs / 2.205:.2f}")
        #return kgs


class Patient:
    
    def __init__(self, name, owner, species, kgs):
        self.name = name
        self.owner = owner
        self.species = species
        self.kgs = kgs
        self.lbs = self.kgs * 2.205
    
    


class Emergency:

    def __init__(self, kgs):

        self.kgs = kgs

        self.atropine4Min = 0
        self.atropine4Max = 0

        self.atropine5Min = 0
        self.atropine5Max = 0

        self.dexamethasoneSPMin = 0
        self.dexamethasoneSPMax = 0

        self.diphenhydramineMax = 0
        self.diphenhydramineMin = 0

        self.ephedrineMin = 0
        self.ephedrineMax = 0

        self.glycopyrrolateMin = 0
        self.glycopyrrolateMax = 0
    

    def atropine(self):
        self.atropineMin = self.kgs * 0.02 / 0.54
        self.atropineMax = self.kgs * 0.04 / 0.54
    
    def dexamethasoneSP(self):
        self.dexamenthasoneSPMin = self.kgs / 4
        self.dexamenthasoneSPMax = self.kgs
    
    def diphenhydramine(self):
        self.diphenhydramineMax = self.kgs / 50
        self.diphenhydramineMin = self.kgs * 2.2 / 50
        return self.diphenhydramineMax

    def ephedrine(self):
        self.ephedrineMin = self.kgs * 0.05 / 50
        self.ephedrineMax = self.kgs * 0.1 / 50

    def glycopyrrolate(self):
        self.glycopyrrolateMin = self.kgs * 0.005 / 0.2
        self.glycopyrrolateMax = self.kgs * 0.01 / 0.2




class AdvancedLifeSupport:
    def __init__(self,kgs):
        self.kgs = kgs

        self.atipamezoleMin = 0
        self.atipamezoleMax = 0

        self.flumazenil = 0

        self.naloxone = 0

        self.atropine4 = 0

        self.atropine5 = 0

        self.epinephrineMin = 0
        self.epinephrineMax = 0

        self.amiodarone = 0

        self.lidocaineCMin = 0
        self.lidocaineCMax = 0

        self.lidocaineF = 0

    def atipamezole(self):
        self.atipamezoleMin = self.kgs * 0.05 / 5
        self.atipamezoleMax = self.kgs * 0.1 / 5

    def flumazenil(self):
        self.flumazenilMin = self.kgs * 0.01 / 0.1

    def naloxone(self):
        self.naxolone = self.kgs * 0.04 / 0.4
    
    def atropine4(self):
        self.atropine4 = self.kgs * 0.05 / 0.4
    
    def atropine5(self):
        self.atropine5 = self.kgs * 0.05 / 0.54
    
    def epinephrine(self):
        self.epinephrineMin = self.kgs * 0.01
        self.epinephrineMax = self.kgs * 0.1
    
    def amiodarone(self):
        self.amiodarone = self.kgs * 5 / 50

    def lidocaineC(self):
        self.lidocaineCMin = self.kgs * 2 / 20
        self.lidocaineCMax = self.kgs * 4 / 20

    def lidocaineF(self):
        self.lidocaineF = self.kgs * 0.2 / 20