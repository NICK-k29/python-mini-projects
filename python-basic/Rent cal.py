#for Rent Calculator 
rent = int(input("enter your room rent = "))
food = int(input("enter of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int (input("enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill)  // persons

print("person will pay = ",output)