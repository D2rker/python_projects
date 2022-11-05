print("Welcome to the tip calcultor")

bill = float(input("What was the total bill : "))
tip = int(input("How much tip would you like to give? 0, 5, 10 :"))
people = int(input("how many people to spilit the bill : "))

bill_with_tip = tip / 100 * bill + bill
bill_with_person = bill_with_tip / people
final = round(bill_with_person,2)
print(f"each person should pay {final}.")
final = "{:.2f}".format(bill_with_person)