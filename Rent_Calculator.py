
Room_Rent = int(input("Enter the amount of rent for the Room/Flat :"))
person = int(input("Enter the number of people living with you :"))
Electricity_per_unit = int(input("What is the elcetricity per unit charge of your Room/Flat :"))
Electricity_Used = int(input("What is the amount of electricity used :"))
Food_Ordered = int(input("what is the amount of food ordered :"))

Total_Elcetricity_Bill = Electricity_per_unit*Electricity_Used

Total_Bill = Room_Rent + Total_Elcetricity_Bill + Food_Ordered

Total_Bill_per_Person = Total_Bill / person

print("Toatl rent for the Room /Flat is = ",Total_Bill)
print("Total rent per person is = ", Total_Bill_per_Person)