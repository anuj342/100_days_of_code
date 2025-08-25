import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

simple_pwd = input("Do you want to make your pwd simple? type yes or no\n")

rand_letters = []
for letter in range(nr_letters):
    rand_letters.append(random.choice(letters))

rand_numbers = []
for number in range(nr_numbers):
    rand_numbers.append(random.choice(numbers))

rand_symbols = []
for symbol in range(nr_symbols):
    rand_symbols.append(random.choice(symbols))

pwd = rand_letters + rand_numbers + rand_symbols
print(pwd)

if simple_pwd == 'yes':
    pwd_new = ''.join(pwd)
    print(pwd_new)
else:
    random.shuffle(pwd)
    hard_pwd = ''.join(pwd)
    print(hard_pwd)

