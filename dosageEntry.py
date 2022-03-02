from tkinter import *

class PatientInfoEntry(Frame):
    def __init__(self,master,callback_on_selected):
        self.species = ""
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.callback_on_selected = callback_on_selected

    def create_widgets(self):
        Label(self, text = "DOSAGE CALCULATOR", font = "Impact 24", fg = "#56b2e8").grid(row = 0, column = 0, columnspan = 2, padx = (20, 0))

        Label(self, text = "Patient Name:").grid(row = 1, column = 0, sticky = E)
        self.patient_ent = Entry(self)
        self.patient_ent.grid(row = 1, column = 1)

        Label(self, text = "Owner Name:").grid(row = 2, column = 0, sticky = E)
        self.owner_ent = Entry(self)
        self.owner_ent.grid(row = 2, column = 1)

        Label(self, text = "Select Species", fg = "#56b2e8", font = "Arial 10 underline").grid(row = 0, column = 3, sticky = S)
        speciesList = ["Canine", "Feline"]
        row_value = 1
        self.species = StringVar()
        self.species.set(None)

        for animal in speciesList:
            Radiobutton(self, text = animal, variable = self.species, value = animal).grid(row = row_value, column = 3)
            row_value += 1
        
        Label(self, text = "Select Weight Unit", fg = "#56b2e8", font = "Arial 10 underline").grid(row = 0, column = 4, sticky = S)
        weightList = ["kgs", "lbs"]
        row_value = 1
        self.weight = StringVar()
        self.weight.set(None)

        for i in weightList:
            Radiobutton(self, text = i, variable = self.weight, value = i).grid(row = row_value, column = 4)
            row_value += 1

        Label(self, text = "Injectable Perianesthetic Medications for canine/feline")

        Label(self, text = "Weight:").grid(row = 4, column = 0)
        self.weight_ent = Entry(self)

        self.weight_ent.grid(row = 4, column = 1)

        Label(self, text = "").grid(row = 3, column = 3)

        Button(self, text = "Submit", bg = "#56b2e8", command = self.on_button_press).grid(row = 4, column = 3)


    def on_button_press(self):
        
        self.callback_on_selected(self.patient_ent.get(), self.owner_ent.get(), self.species.get(), self.weight_ent.get())



