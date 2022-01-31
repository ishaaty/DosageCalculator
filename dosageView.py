#from dosageCalculations import Patient, Emergency

from dosageCalculations import *

def main():

    print("\nThis is the ULTIMATE DOSAGE CALCULATOR created by ishaaaaa\n")

    name = input("What is the patient's name? ")
    owner = input("What is the owner's name? ")
    species = input("Is the patient a feline or canine? ")
    weight = input("Enter the patient's weight in lbs or kgs: ")
    
    a = Patient(name, owner, species, weight)
    print(a)

    a1 = Emergency(weight)
    print(a1.diphenhydramine())


main()