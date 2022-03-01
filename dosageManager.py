from tkinter import *

from dosageEntry import PatientInfoEntry
from dosageTableView import Application

class DosageManager():
    def __init__(self):
        self.root = Tk()
        self.screen = None

        frame_main = Frame(self.root)
        frame_main.grid(sticky='news')  

    def displayPatientIntroEntry(self):
        self.root.title("Patient Information")
        self.root.geometry("490x175")
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
        self.root.geometry("1200x900")
        self.screen = Application(master = self.root, patient = self.patient, owner = self.owner, species = self.species, weight = self.weight, callback_on_close = self.close_GUI, callback_on_entry = self.new_entry)
        self.root.config()
        
        


    def close_GUI(self):
        self.root.destroy()

    def new_entry(self):
        self.screen.destroy()
        self.displayPatientIntroEntry()

def main():
    calc = DosageManager()
    calc.displayPatientIntroEntry()
    calc.root.mainloop()

main()
