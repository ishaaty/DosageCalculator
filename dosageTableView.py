#from dosageCalculations import Patient, Emergency
from dosageCalculations import *
from tkinter import *

from dosageEntry import PatientInfoEntry 


class Application(Frame):

    def __init__(self, master, patient, owner, species, weight, callback_on_close, callback_on_entry):

        super().__init__(master)

        self.grid()

        self.kgs = weight
        self.ownerName = owner
        self.petName = patient
        self.species = species
        self.callback_on_close = callback_on_close
        self.callback_on_entry = callback_on_entry

        self.create_widgets_generalInfo(master)
        self.create_widgets_buttons()        
        self.create_widgets_scrollbar(master)        
        self.create_widgets_emergency()
        self.create_widgets_ALS()
        self.create_widgets_anesthesia()
    

    def create_widgets_generalInfo(self):
        
        self.gen_info = Frame(bg = "#56b2e8", width = 12)
        self.gen_info.grid(row = 0, column = 0, sticky = EW)

        Label(self.gen_info, text = "DOSAGE CALCULATOR: Felines & Canines", font = "Impact 24", fg = "white", bg= "#56b2e8").grid(row = 0, column = 0, columnspan = 4, sticky = W, padx = 20, pady =(10, 5))


        # patient Name
        patientName = Label(self.gen_info, text = "Patient Name: " + self.petName, font = "Arial 10 bold")
        patientName.grid(row = 1, column = 0, columnspan = 2, sticky = W, padx = 20)

        # owner Name
        ownerName = Label(self.gen_info, text = "Owner Name: " + self.ownerName, font = "Arial 10 bold")
        ownerName.grid(row = 2, column = 0, columnspan = 2, sticky = W, padx = 20, pady = (0,10))

        # species
        species = Label(self.gen_info, text = "Species: " + self.species, font = "Arial 10 bold")
        species.grid(column = 2, row = 1, columnspan = 2, sticky = W)

        # body weight kgs
        kgs = Label(self.gen_info, text = "Body Weight(kgs): " + self.kgs, font = "Arial 10 bold")
        kgs.grid(column = 2, row = 2, columnspan = 2, sticky = W)

        self.table_frame = Frame(master)
        self.table_frame.grid(row = 3, column = 0)
        self.table_frame.grid_rowconfigure(0, weight = 1)
        self.table_frame.grid_columnconfigure(0, weight = 1)

        self.canvas = Canvas(self.table_frame)
        self.canvas.grid(row = 3, column = 0, sticky = "NEWS")


    def create_widgets_emergency(self):

        Label(self.inner_frame, text = "Emergency Medications", bg = "#56b2e8", font = "Impact 12", fg = "white", relief = "solid", bd = 1).grid(row = 3, column = 0, columnspan = 6, sticky = W+E, padx = (20,0), pady = (10, 0))
        self.table_frame.grid(row = 3, column = 0)

        Label(self.inner_frame, text = "Drug", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 4, rowspan = 2, column = 0, sticky = W+E+N+S, padx = (20,0))

        Label(self.inner_frame, text = "Conc. mg/mL", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 4, rowspan = 2, column = 1, sticky = W+E+N+S)

        Label(self.inner_frame, text = "Range mg/kg", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 4, rowspan = 2, column = 2, sticky = W+E+N+S)

        Label(self.inner_frame, text = "Species", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1 ).grid(row = 4, rowspan = 2, column = 3, sticky = W+E+N+S)
    
        Label(self.inner_frame, text = "Volume (mLs)", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1 ).grid(row = 4, column = 4, columnspan = 2, sticky = W+E+N+S)

        Label(self.inner_frame, text = "Minimum", bg = "white", relief = "solid", bd = 1).grid(row = 5, column = 4, sticky = W+E+N+S)

        Label(self.inner_frame, text = "Maximum", bg = "white", relief = "solid", bd = 1).grid(row = 5, column = 5, sticky = W+E+N+S)

                       
        # fix this code v
        f = open("namesEmergency.txt")
        row_num = 6
        column_num = 0
        x = 20


        for line in f:
            l = line.split("; ")
            x = 20
            for item in l:
                Label(self.inner_frame, text = item, bg = "white", relief = "solid", bd = 1).grid(row = row_num, column = column_num, sticky = W+E+N+S, padx = (x, 0))
                if x == 20:
                    x = 0
                column_num += 1
            row_num += 1
            column_num = 0

        row_num = 6
        column_num = 4

    
        for num in Emergency(float(self.kgs)).returnMedicineList():
            num = f"{num:.2f}"
            l = Label(self.inner_frame, text = num, bg = "white", relief = "solid", bd = 1)
            if column_num % 2 == 0:
                l.grid(row = row_num, column = column_num, sticky = W+E+N+S)
                row_num += 1
            else:
                l.grid(row = row_num - 1, column = column_num, sticky = W+E+N+S)
            if column_num == 5:
                column_num = 4
            else:
                column_num += 1
            

            

    def create_widgets_ALS(self):
        Label(self.inner_frame, text = "Advanced Life Support (ALS) Medications", bg = "#56b2e8", font = "Impact 12", fg = "white", relief = "solid", bd = 1).grid(row = 12, column = 0, columnspan = 6, sticky = W+E, padx = (20,0), pady = (10,0))

        Label(self.inner_frame, text = "Drug", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 13, rowspan = 2, column = 0, sticky = W+E+N+S, padx = (20,0))

        Label(self.inner_frame, text = "Conc. mg/mL", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 13, rowspan = 2, column = 1, sticky = W+E+N+S)

        Label(self.inner_frame, text = "Range mg/kg", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 13, rowspan = 2, column = 2, sticky = W+E+N+S)

        Label(self.inner_frame, text = "Species", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 13, rowspan = 2, column = 3, sticky = W+E+N+S)
    
        Label(self.inner_frame, text = "Volume (mLs)", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 13, column = 4, columnspan = 2, sticky = W+E+N+S)

        Label(self.inner_frame, text = "Minimum", bg = "white", relief = "solid", bd = 1).grid(row = 14, column = 4, sticky = W+E+N+S)

        Label(self.inner_frame, text = "Maximum", bg = "white", relief = "solid", bd = 1).grid(row = 14, column = 5, sticky = W+E+N+S)

        f = open("namesALS.txt")
        row_num = 15
        column_num = 0
        x = 20


        for line in f:
            l = line.split("; ")
            x = 20
            for item in l:
                Label(self.inner_frame, text = item, bg = "white", relief = "solid", bd = 1).grid(row = row_num, column = column_num, sticky = W+E+N+S, padx = (x, 0))
                if x == 20:
                    x = 0
                column_num += 1
            row_num += 1
            column_num = 0

        row_num = 15
        column_num = 4

        i = 0
        for num in AdvancedLifeSupport(float(self.kgs)).returnList():
            if num == 0:
                l = Label(self.inner_frame, text = "", bg = "#56b2e8", relief = "solid", bd = 1)
            else:
                num = f"{num:.2f}"
                l = Label(self.inner_frame, text = num, bg = "white", relief = "solid", bd = 1)
            if column_num % 2 == 0:
                l.grid(row = row_num, column = column_num, sticky = W+E+N+S)
                row_num += 1
            else:
                l.grid(row = row_num - 1, column = column_num, sticky = W+E+N+S)
            if column_num == 5:
                column_num = 4
            else:
                column_num += 1
    

    def create_widgets_anesthesia(self):

        Label(self.inner_frame, text = "Anesthesia and Analegesia Medications", bg = "#56b2e8", font = "Impact 12", fg = "white", relief = "solid", bd = 1).grid(row = 3, column = 6, columnspan = 6, sticky = W+E, padx = (20,0), pady = (10,0))

        Label(self.inner_frame, text = "Drug", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 4, rowspan = 2, column = 6, sticky = W+E+N+S, padx = (20,0))

        Label(self.inner_frame, text = "Conc. mg/mL", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 4, rowspan = 2, column = 7, sticky = W+E+N+S)

        Label(self.inner_frame, text = "Range mg/kg", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 4, rowspan = 2, column = 8, sticky = W+E+N+S)

        Label(self.inner_frame, text = "Species", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 4, rowspan = 2, column = 9, sticky = W+E+N+S)
    
        Label(self.inner_frame, text = "Volume (mLs)", bg = "white", font = "Arial 9 bold", relief = "solid", bd = 1).grid(row = 4, column = 10, columnspan = 2, sticky = W+E+N+S)

        Label(self.inner_frame, text = "Minimum", bg = "white", relief = "solid", bd = 1).grid(row = 5, column = 10, sticky = W+E+N+S)

        Label(self.inner_frame, text = "Maximum", bg = "white", relief = "solid", bd = 1).grid(row = 5, column = 11, sticky = W+E+N+S)

        f = open("anesthesiaAnalgesiaFile.txt")
        row_num = 6
        column_num = 6
        x = 20

        for line in f:
            l = line.split("; ")
            x = 20
            for item in l:
                Label(self.inner_frame, text = item, bg = "white", relief = "solid", bd = 1).grid(row = row_num, column = column_num, sticky = W+E+N+S, padx = (x, 0))
                if x == 20:
                    x = 0
                column_num += 1
            row_num += 1
            column_num = 6

        row_num = 6
        column_num = 10


        for num in anesthesiaAnalgesia(float(self.kgs)).returnMedicine():
            if num == 0:
                l = Label(self.inner_frame, text = "", bg = "#56b2e8", relief = "solid", bd = 1)
            else:
                num = f"{num:.2f}"
                l = Label(self.inner_frame, text = num, bg = "white", relief = "solid", bd = 1)
            if column_num % 2 == 0:
                l.grid(row = row_num, column = column_num, sticky = W+E+N+S)
                row_num += 1
            else:
                l.grid(row = row_num - 1, column = column_num, sticky = W+E+N+S)
            if column_num == 11:
                column_num = 10
            else:
                column_num += 1


    def create_widgets_scrollbar(self, master):
        self.scrollbar = Scrollbar(self.table_frame, orient = VERTICAL, command = self.canvas.yview)
        self.scrollbar.grid(row = 3, column = 1, sticky = NS)
        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.canvas.configure(height = 650, width = 1000)

        self.inner_frame = Frame(self.canvas)
        self.canvas.create_window((0,0), window = self.inner_frame, anchor = NW)

        self.inner_frame.update_idletasks()
        self.canvas.config(scrollregion = self.canvas.bbox("all"))
    
    def create_widgets_buttons(self):
        Button(self.gen_info, text = "Close Form", bg = "white", font = "Arial 8 bold", command = self.form_closed).grid(row = 0, column = 7)
        Button(self.gen_info, text = "Enter Patient Info", bg = "white", font = "Arial 8 bold", command = self.enter_patient_info).grid(row = 1, column = 7)

    def form_closed(self):
        self.callback_on_close()
    
    def enter_patient_info(self):
        self.callback_on_entry()

def main():
    root = Tk()
    root.title("Dosage Table") 
    root.geometry("500x500")
    app = Application(root)

    root.mainloop()

#main()






