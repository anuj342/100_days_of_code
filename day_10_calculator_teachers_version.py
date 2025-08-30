def add(n1, n2):
    return n1+n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1,n2):
    return n1 - n2

operation_symbol = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    accumulate = True
    num1 = float(input("Enter the first number:    "))
    while accumulate:
        for symbol in operation_symbol:
            print(symbol)
        operation = input("Enter the operation:")
        num2 = float(input("Enter the second number"))
        output = operation_symbol[operation](num1, num2)
        print(f"The result is: {output}")
        choice = input("Would you like to calculate again with the same number? (y/n):")
        if choice == "y":
            num1 = output
        else:
            accumulate = False
            print("\n" * 20)
            calculator()

calculator()