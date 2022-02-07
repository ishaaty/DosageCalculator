from tkinter import *

from dosageEntry import PatientInfoEntry
from dosageTableView import Application
from dosageCalculations import Patient, Emergency, anesthesiaAnalgesia, AdvancedLifeSupport

class DosageManager():
    def __init__(self):
        self.root = Tk()
        self.screen = None

    def displayPatientIntroEntry(self):
        self.root.title("Patient Information")
        self.screen = PatientInfoEntry(master = self.root, callback_on_selected = self.onclose_PatientIntroEntry)

    def onclose_PatientIntroEntry(self, patient, owner, species, weight):
        self.patient = patient
        self.owner = owner
        self.species = species
        self.weight = weight

        self.screen.destroy()

        self.displayDosageTable()

    def displayDosageTable(self):
        self.root.title("Dosages")
        self.screen = Application(master = self.root)

def main():
    calc = DosageManager()
    calc.displayPatientIntroEntry()
    calc.root.mainloop()

main()