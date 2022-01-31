
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




