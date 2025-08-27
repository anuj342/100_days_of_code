logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bidders = {}

while True:
    name=input("Enter your name: ")
    your_bid = int(input("Enter your bid: "))
    other = input("Is there anyone remaining: ").lower()
    
    bidders[name] = your_bid

    if other == "yes":
        print("\n " * 100)
    elif other == "no":
        max_value = max(bidders.values())
        break
    else:
        print("Invalid input")
print(f"The highest bid is of {max_value} by {name}")
print(bidders)