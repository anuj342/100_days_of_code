print("Welcome to the tip calculator!")
total = float(input("What is the total bill: "))
tip = int(input("How much bill would u like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill into: "))
splitted_bill = (total + tip) / number_of_people
print(f"Each person should pay: {splitted_bill}")