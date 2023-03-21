
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

    def __init__(self, kgs, species):

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

        self.emergencyList = [self.atropine4Min, self.atropine4Max, self.atropine5Min, 
                            self.atropine5Max, self.dexamenthasoneSPMin, self.dexamenthasoneSPMax, 
                            self.diphenhydramineMin, self.diphenhydramineMax, self.ephedrineMin, 
                            self.ephedrineMax, self.glycopyrrolateMin, self.glycopyrrolateMax]

    def returnMedicineList(self):
        for num in self.emergencyList:
            num = float(num)
            num = f"{num:.2f}"
        return self.emergencyList

    


class anesthesiaAnalgesia:

    def __init__(self, kgs, species):

        self.kgs = kgs

        if species == "Canine":
            self.acepromazineCMin = self.kgs * 0.005
            self.acepromazineCMax = self.kgs * 0.05
        else:
            self.acepromazineCMin = 0
            self.acepromazineCMax = 0

        if species == "Feline":
            self.acepromazineFMin = self.kgs * 0.01
            self.acepromazineFMax = self.kgs * 0.1
        else:
            self.acepromazineFMin = 0
            self.acepromazineFMax = 0

        self.alfaxaloneMin = self.kgs / 10
        self.alfaxaloneMax = self.kgs * 4 / 10

        self.atipamezoleMin = self.kgs * 0.05 / 5
        self.atipamezoleMax = 0

        if species == "Feline":
            self.atipamezoleFMin = self.kgs * 0.012 / 5
            self.atipamezoleFMax = self.kgs * 0.021 / 5
        else:
            self.atipamezoleFMin = 0
            self.atipamezoleFMax = 0

        if species == "Canine":
            self.bupivacaineCMax = self.kgs * 2 / 5
            self.bupivacaineCMin = self.kgs / 5
        else:
            self.bupivacaineCMax = 0
            self.bupivacaineCMin = 0
        
        if species == "Feline":
            self.bupivacaineFMin = self.kgs / 5
            self.bupivacaineFMax = self.kgs * 1.5 / 5

        else:
            self.bupivacaineFMin = 0
            self.bupivacaineFMax = 0

        if species == "Canine":
            self.buprenorophineCMax = self.kgs * 0.02 / 0.3
            self.buprenorophineCMin = self.kgs * 0.005 / 0.3
        else:
            self.buprenorophineCMax = 0
            self.buprenorophineCMin = 0

        if species == "Feline":
            self.buprenorophineFMax = self.kgs * 0.02 / 0.3
            self.buprenorophineFMin = self.kgs * 0.01 / 0.3
        else:
            self.buprenorophineFMax = 0 
            self.buprenorophineFMin = 0

        if species == "Feline":
            self.buprenorphineLAMin = self.kgs * 0.24 / 1.8
        else:
            self.buprenorphineLAMin = 0
        self.buprenorphineLAMax = 0

        self.butorphanelMax = self.kgs * 0.4 / 10
        self.butorphanelMin = self.kgs * 0.2 / 10

        if species == "Canine":
            self.carprofenMin = self.kgs * 4 / 50
            self.carprofenMax = self.kgs * 4.4 / 50
        else:
            self.carprofenMin = 0
            self.carprofenMax = 0

        if species == "Canine":
            self.dexmedetomidineCMax = self.kgs * 0.02 / 0.5
            self.dexmedetomidineCMin = self.kgs * 0.005 / 0.5
        else:
            self.dexmedetomidineCMin = 0
            self.dexmedetomidineCMax = 0
            
        if species == "Feline":
            self.dexmedetomidineFMin = self.kgs * 0.005 / 0.5
            self.dexmedetomidineFMax = self.kgs * 0.01 / 0.5

        else:
            self.dexmedetomidineFMin = 0
            self.dexmedetomidineFMax = 0

        if species == "Feline":
            self.DKTmixtureMin = self.kgs * 0.035
            self.DKTmixtureMax = self.kgs * 0.065 
        else:
            self.DKTmixtureMin = 0
            self.DKTmixtureMax = 0 

        self.fentanylMin = self.kgs * 0.003 / 0.05
        self.fentanylMax = self.kgs * 0.005 / 0.05

        if species == "Canine":
            self.hydromorphoneCMin = self.kgs * 0.05 / 2
            self.hydromorphoneCMax = self.kgs * 0.2 / 2
        else:
            self.hydromorphoneCMin = 0
            self.hydromorphoneCMax = 0

        if species == "Feline":
            self.hydromorphoneFMin = self.kgs * 0.05 / 2 
            self.hydromorphoneFMax = self.kgs * 0.1 / 2
        else:
            self.hydromorphoneFMin = 0 
            self.hydromorphoneFMax = 0

        if species == "Canine":
            self.ketamineMax = self.kgs * 2 / 100
            self.ketamineMin = self.kgs / 100
        else:
            self.ketamineMax = 0
            self.ketamineMin = 0
        ##################
        if species == "Canine":
            self.lidocaineMaxCA = self.kgs * 4 / 20
            self.lidocaineMinCA = self.kgs / 20
            self.lidocaineMinFA = 0
            self.lidocaineMaxFA = 0
        
        if species == "Feline":
            self.lidocaineMinFA = self.kgs / 20
            self.lidocaineMaxFA = self.kgs * 2 / 20
            self.lidocaineMinCA = 0
            self.lidocaineMaxCA = 0
        #################
        self.maropitantCitrateMin = self.kgs / 10
        self.maropitantCitrateMax = 0

        if species == "Canine":
            self.meloxicamCMin = self.kgs * 0.2 / 5
            self.meloxicamCMax = 0
        else:
            self.meloxicamCMin = 0
            self.meloxicamCMax = 0

        if species == "Feline":
            self.meloxicamFMin = self.kgs * 0.3 / 5
            self.meloxicamFMax = 0
        else:
            self.meloxicamFMin = 0
            self.meloxicamFMax = 0

        self.midazolam1Min = self.kgs * 0.1
        self.midazolam1Max = self.kgs * 0.3

        self.midazolam5Min = self.kgs * 0.1 / 5
        self.midazolam5Max = self.kgs * 0.3 / 5
        
        self.propofolMin = self.kgs / 10
        self.propofolMax = self.kgs * 8 / 10

        self.robenacoxibMin = self.kgs * 2 / 20
        self.robenacoxibMax = 0

        self.tiletaminZolazepamMin = self.kgs / 100
        self.tiletaminZolazepamMax = self.kgs * 4 / 100
        

        self.anesthesiaList = [self.acepromazineCMin, self.acepromazineCMax,
                            self.acepromazineFMin, self.acepromazineFMax, self.alfaxaloneMin, 
                            self.alfaxaloneMax, self.atipamezoleMin, self.atipamezoleMax, self.atipamezoleFMin,
                            self.atipamezoleFMax, self.bupivacaineCMin, self.bupivacaineCMax, 
                            self.bupivacaineFMin, self.bupivacaineFMax, 
                            self.buprenorophineCMin, self.buprenorophineCMax, self.buprenorophineFMin,
                            self.buprenorophineFMax, self.buprenorphineLAMin, self.buprenorphineLAMax, self.butorphanelMin,
                            self.butorphanelMax, self.carprofenMin, self.carprofenMax, 
                            self.dexmedetomidineCMin, self.dexmedetomidineCMax, 
                            self.dexmedetomidineFMin, self.dexmedetomidineFMax, self.DKTmixtureMin, 
                            self.DKTmixtureMax, self.fentanylMin, self.fentanylMax, 
                            self.hydromorphoneCMin, self.hydromorphoneCMax, self.hydromorphoneFMin, 
                            self.hydromorphoneFMax, self.ketamineMin, self.ketamineMax,
                            self.lidocaineMinCA, self.lidocaineMaxCA, self.lidocaineMinFA, self.lidocaineMaxFA,self.maropitantCitrateMin, self.maropitantCitrateMax, 
                            self.meloxicamCMin, self.meloxicamCMax, self.meloxicamFMin, self.meloxicamFMax, self.midazolam1Min,
                            self.midazolam1Max, self.midazolam5Min, self.midazolam5Max, 
                            self.propofolMin, self.propofolMax, self.robenacoxibMin, self.robenacoxibMax, 
                            self.tiletaminZolazepamMin, self.tiletaminZolazepamMax]

    def returnMedicine(self):
        for num in self.anesthesiaList:
            num = float(num)
            num = f"{num:.2f}"
        return self.anesthesiaList

        






class AdvancedLifeSupport:

    def __init__(self,kgs, species):

        self.kgs = kgs

        self.atipamezoleMin = self.kgs * 0.05 / 5
        self.atipamezoleMax = self.kgs * 0.1 / 5

        self.flumazenilMin = self.kgs * 0.01 / 0.1
        self.flumazenilMax = False

        self.naxoloneMin = self.kgs * 0.04 / 0.4
        self.naxoloneMax = False

        self.atropine4Min = self.kgs * 0.05 / 0.4
        self.atropineMax = False

        self.atropine5Min = self.kgs * 0.05 / 0.54
        self.atropine5Max = False

        self.epinephrineMin = self.kgs * 0.01
        self.epinephrineMax = self.kgs * 0.1

        self.amiodaroneMin = self.kgs * 5 / 50
        self.amiodaroneMax = False
        
        if species == "Canine":
            self.lidocaineCMin = self.kgs * 2 / 20
            self.lidocaineCMax = self.kgs * 4 / 20
        else:
            self.lidocaineCMin = 0
            self.lidocaineCMax = 0
        if species == "Feline":
            self.lidocaineFMin = self.kgs * 0.2 / 20
            self.lidocaineFMax = False
        else:
            self.lidocaineFMin = 0
            self.lidocaineFMax = 0

        self.ALSList = [self.atipamezoleMin, self.atipamezoleMax, self.flumazenilMin, 
                        self.flumazenilMax, self.naxoloneMin, self.naxoloneMax, self.atropine4Min, 
                        self.atropineMax, self.atropine5Min, self.atropine5Max, self.epinephrineMin, 
                        self.epinephrineMax, self.amiodaroneMin, self.amiodaroneMax, self.lidocaineCMin, 
                        self.lidocaineCMax, self.lidocaineFMin,self.lidocaineFMax]

    def returnList(self):
        return self.ALSList

     
