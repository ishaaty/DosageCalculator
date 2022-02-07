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

