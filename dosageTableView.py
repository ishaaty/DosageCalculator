#from dosageCalculations import Patient, Emergency
from dosageCalculations import *
from tkinter import *

from dosageEntry import PatientInfoEntry 


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
        Label(self, text = "DOSAGE CALCULATOR: Felines & Canines", font = "Impact 24", fg = "#56b2e8").grid(row = 0, column = 0, columnspan = 5, sticky = W, padx = 20, pady =(10, 5))



        # patient Name
        patientName = Label(self, text = "Patient Name: " + "name")
        patientName.grid(row = 1, column = 0, columnspan = 2, sticky = W, padx = 20)

        # owner Name
        ownerName = Label(self, text = "Owner Name: " + "name")
        ownerName.grid(row = 2, column = 0, columnspan = 2, sticky = W, padx = 20, pady = (0,10))

        # species
        species = Label(self, text = "Species: " + "species")
        species.grid(column = 2, row = 1, columnspan = 2, sticky = W)

        # body weight kgs
        kgs = Label(self, text = "Body Weight(kgs): " + "kgs")
        kgs.grid(column = 2, row = 2, columnspan = 2, sticky = W)



    def create_widgets_emergency(self):

        Label(self, text = "Emergency", bg = "#56b2e8", font = "Impact 12", fg = "white", relief = "solid", bd = 1).grid(row = 3, column = 0, columnspan = 6, sticky = W+E, padx = (20,0))

        Label(self, text = "Drug", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 4, rowspan = 2, column = 0, sticky = W+E+N+S, padx = (20,0))

        Label(self, text = "Conc. mg/mL", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 4, rowspan = 2, column = 1, sticky = W+E+N+S)

        Label(self, text = "Range mg/kg", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 4, rowspan = 2, column = 2, sticky = W+E+N+S)

        Label(self, text = "Species", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 4, rowspan = 2, column = 3, sticky = W+E+N+S)
    
        Label(self, text = "Volume (mLs)", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 4, column = 4, columnspan = 2, sticky = W+E+N+S)

        Label(self, text = "Minimum", bg = "white", relief = "solid", bd = 1).grid(row = 5, column = 4, sticky = W+E+N+S)

        Label(self, text = "Maximum", bg = "white", relief = "solid", bd = 1).grid(row = 5, column = 5, sticky = W+E+N+S)

                       
        # fix this code v
        f = open("namesEmergency.txt")
        row_num = 6
        column_num = 0
        x = 20


        for line in f:
            l = line.split("; ")
            x = 20
            for item in l:
                Label(self, text = item, bg = "white", relief = "solid", bd = 1).grid(row = row_num, column = column_num, sticky = W+E+N+S, padx = (x, 0))
                if x == 20:
                    x = 0
                column_num += 1
            row_num += 2
            column_num = 0
        


        row_num = 6
        column_num = 4

        i = 0
        for num in Emergency(13.61).returnMedicineList():
            num = f"{num:.2f}"
            l = Label(self, text = num, bg = "white", relief = "solid", bd = 1)
            if row_num % 2 == 0:
                l.grid(row = row_num, column = column_num, sticky = W+E+N+S)
            else:
                l.grid(row = row_num - 1, column = column_num, sticky = W+E+N+S)
            row_num += 1
            i += 1
            if column_num == 5:
                column_num = 4
            else:
                column_num += 1
            

            

    def create_widgets_ALS(self):
        # TODO
        pass
    

    def create_widgets_anesthesia(self):
        # TODO
        pass








