#from dosageCalculations import Patient, Emergency
from dosageCalculations import *
from tkinter import * 


class Application(Frame):

    def __init__(self, master):

        super().__init__(master)
        self.grid()
        self.create_widgets_generalInfo()
        self.create_widgets_emergency()
        self.create_widgets_ALS()
        self.create_widgets_anesthesia
    
    def create_widgets_generalInfo(self):
        # TODO
        Label(self, text = "DOSAGE CALCULATOR", font = "Impact 24", fg = "#56b2e8").grid(row = 0, column = 0, columnspan = 3, sticky = W)
        Label(self, text = "Injectable Perianesthetic Medications for canine/feline", font = "Arial 9").grid(row = 0, column = 3, columnspan = 3, sticky = E)

        # patient Name
        patientName = Label(self, text = "Patient Name: " + "name")
        patientName.grid(row = 1, column = 0, columnspan = 3, sticky = W)

        # owner Name
        ownerName = Label(self, text = "Owner Name: " + "name")
        ownerName.grid(row = 2, column = 0, columnspan = 3, sticky = W)

        # species
        species = Label(self, text = "Species: " + "species")
        species.grid(column = 3, row = 1, columnspan = 3, sticky = W)

        # body weight kgs
        kgs = Label(self, text = "Body Weight(kgs): " + "kgs")
        kgs.grid(column = 3, row = 2, columnspan = 3, sticky = W)



    def create_widgets_emergency(self):

        Label(self, text = "Emergency", bg = "#56b2e8", font = "Impact 11", fg = "white", relief = "solid", bd = 1).grid(row = 3, column = 0, columnspan = 3, sticky = W+E)

        Label(self, text = "Drug/Concentration/Dose Range", bg = "white", font = "Arial 13", relief = "solid", bd = 1).grid(row = 4, rowspan = 2, column = 0, sticky = W+E+N+S)
        
        Label(self, text = "Volume (mLs)", bg = "white", relief = "solid", bd = 1).grid(row = 4, column = 1, columnspan = 2, sticky = W+E)

        Label(self, text = "Minimum", bg = "white", relief = "solid", bd = 1).grid(row = 5, column = 1)

        Label(self, text = "Maximum", bg = "white", relief = "solid", bd = 1).grid(row = 5, column = 2)

                       
        # fix this code v

        
        Label(self, text = "Atropine (0.4 mg/mL) (0.02 - 0.04 mg/kg)", bg = "white", relief = "solid", bd = 1).grid(row = 6, rowspan = 2, column = 0, sticky = W+E+N+S)

        atropineMin4 = Label(self, bg = "white", relief = "solid", bd = 1)
        atropineMin4.grid(row = 6, rowspan = 2, column = 1, sticky = W+E+N+S)

        atropineMax4 = Label(self, bg = "white", relief = "solid", bd = 1)
        atropineMax4.grid(row = 6, rowspan = 2, column = 2, sticky = W+E+N+S)

        Label(self, text = "Atropine (0.54 mg/mL) (0.02 - 0.04 mg/kg)", bg = "white", relief = "solid", bd = 1).grid(row = 8, rowspan = 2, column = 0, sticky = W+E+N+S)

        atropineMin5 = Label(self, bg = "white", relief = "solid", bd = 1)
        atropineMin5.grid(row = 8, rowspan = 2, column = 1, sticky = W+E+N+S)

        atropineMax5 = Label(self, bg = "white", relief = "solid", bd = 1)
        atropineMax5.grid(row = 8, rowspan = 2, column = 2, sticky = W+E+N+S)

        Label(self, text = "Dexamethasone SP (4 mg/mL) (1 - 4 mg/kg)", bg = "white", relief = "solid", bd = 1).grid(row = 10, rowspan = 2, column = 0, sticky = W+E+N+S)

        Label(self, text = "Diphenhydramine (50 mg/mL) (1 - 2.2 mg/kg)", bg = "white", relief = "solid", bd = 1).grid(row = 12, rowspan = 2, column = 0, sticky = W+E+N+S)

        Label(self, text = "Ephedrine (50 mg/mL) (0.05 - 0.1 mg/kg)", bg = "white", relief = "solid", bd = 1).grid(row = 14, rowspan = 2, column = 0, sticky = W+E+N+S)

        Label(self, text = "Glycopyrrolate (0.2 mg/mL) (0.005 - 0.01 mg/kg)", bg = "white", relief = "solid", bd = 1).grid(row = 16, rowspan = 2, column = 0, sticky = W+E+N+S)



    def create_widgets_ALS(self):
        # TODO
        pass
    
    def create_widgets_anesthesia(self):
        # TODO
        pass


def main():
    root = Tk()
    root.title("Dosage Table")
    root.geometry("700x500")
    app = Application(root)

    root.mainloop()

main()

