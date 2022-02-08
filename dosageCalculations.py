
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

        self.atropine4Min = self.kgs * 0.02 / 0.4
        self.atropine4Max = self.kgs * 0.04 / 0.4

        self.atropine5Min = self.kgs * 0.02 / 0.54
        self.atropine5Max = self.kgs * 0.04 / 0.54

        self.dexamenthasoneSPMin = self.kgs / 4
        self.dexamenthasoneSPMax = self.kgs

        self.diphenhydramineMin = self.kgs / 50
        self.diphenhydramineMax = self.kgs * 2.2 / 50

        self.ephedrineMin = self.kgs * 0.05 / 50
        self.ephedrineMax = self.kgs / 50

        self.glycopyrrolateMin = self.kgs * 0.005 / 0.2
        self.glycopyrrolateMax = self.kgs * 0.01 / 0.2

        self.medicineList = [self.atropine4Min, self.atropine4Max, self.atropine5Min, 
                            self.atropine5Max, self.dexamenthasoneSPMin, self.dexamenthasoneSPMax, 
                            self.diphenhydramineMin, self.diphenhydramineMax, self.ephedrineMin, 
                            self.ephedrineMax, self.glycopyrrolateMin, self.glycopyrrolateMax]

    def returnMedicineList(self):
        return self.medicineList

    


class anesthesiaAnalgesia:

    def __init__(self, kgs):

        self.kgs = kgs

        self.acepromazineCMax = self.kgs * 0.05
        self.acepromazineCMin = self.kgs * 0.005

        self.acepromazineFMax = self.kgs * 0.1
        self.acepromazineFMin = self.kgs * 0.01

        self.alfaxaloneMax = self.kgs * 4 / 10
        self.alfaxaloneMin = self.kgs / 10

        self.atipamezole = self.kgs * 0.05 / 5

        self.atipamezoleFMax = self.kgs * 0.021 / 5
        self.atipamezoleFMin = self.kgs * 0.012 / 5

        self.bupivacaineCMax = self.kgs * 2 / 5
        self.bupivacaineCMin = self.kgs / 5

        self.bupivacaineFMax = self.kgs * 1.5 /5
        self.bupivacaineFMax = self.kgs / 5

        self.buprenorophineCMax = self.kgs * 0.02 / 0.3
        self.buprenorophineCMin = self.kgs * 0.005 / 0.3

        self.buprenorophineFMax = self.kgs * 0.02 / 0.3
        self.buprenorophineFMin = self.kgs * 0.01 / 0.3

        self.buprenorphineLA = self.kgs * 0.24 / 1.8

        self.butorphanelMax = self.kgs * 0.4 / 10
        self.butorphanelMin = self.kgs * 0.2 / 10

        self.carprofenMax = self.kgs * 4.4 / 50
        self.carprofenMin = self.kgs * 4 / 50

        self.dexmedetomidineCMax = self.kgs * 0.005 / 0.5
        self.dexmedetomidineCMin = self.kgs * 0.02 / 0.5

        self.dexmedetomidineFMax = self.kgs * 0.01 / 0.5
        self.dexmedetomidineFMin = self.kgs * 0.005 / 0.5

        self.DKTmixtureMax = ""
        self.DKTmixtureMin = ""

        self.fentanylMax = self.kgs * 0.005 / 0.05
        self.fentanylMin = self.kgs * 0.003 / 0.05

        self.hydromorphoneCMax = self.kgs * 0.2 / 2
        self.hydromorphoneCMin = self.kgs * 0.05 / 2

        self.hydromorphoneFMax = self.kgs * 0.1 / 2
        self.hydromorphoneCMin = self.kgs * 0.05 / 2 
        
        self.ketamineMax = self.kgs * 2 / 100
        self.ketamineMin = self.kgs / 100

        self.lidocaineMax = self.kgs * 4 / 20
        self.lidocaineMin = self.kgs / 20

        self.maropitantCitrate = self.kgs / 10

        self.meloxicamC = self.kgs * 0.2 / 5

        self.meloxicamF = self.kgs * 0.3 / 5

        self.midazolam1Max = self.kgs * 0.3
        self.midazolam1Min = self.kgs * 0.1

        self.midazolam5Max = self.kgs * 0.3 / 5
        self.midazolam5Min = self.kgs * 0.1 / 5

        self.propofolMax = self.kgs * 8 / 10
        self.propofolMin = self.kgs / 10

        self.robenacoxib = self.kgs * 2 / 20

        self.tiletaminZolazepamMax = self.kgs * 4 / 100
        self.tiletaminZolazepamMin = self.kgs / 100



class AdvancedLifeSupport:

    def __init__(self,kgs):

        self.kgs = kgs

        self.atipamezoleMin = self.kgs * 0.05 / 5
        self.atipamezoleMax = self.kgs * 0.1 / 5

        self.flumazenilMin = self.kgs * 0.01 / 0.1

        self.naxolone = self.kgs * 0.04 / 0.4

        self.atropine4 = self.kgs * 0.05 / 0.4

        self.atropine5 = self.kgs * 0.05 / 0.54

        self.epinephrineMin = self.kgs * 0.01
        self.epinephrineMax = self.kgs * 0.1

        self.amiodarone = self.kgs * 5 / 50

        self.lidocaineCMin = self.kgs * 2 / 20
        self.lidocaineCMax = self.kgs * 4 / 20

        self.lidocaineF = self.kgs * 0.2 / 20

     
