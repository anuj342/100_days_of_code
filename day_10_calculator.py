def add(n1, n2):
    return n1+n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1,n2):
    return n1 - n2

operation = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
n1 = int(input("Enter first number: "))
print(operation.keys())
input_operation = input("Enter operation: ")
n2 = int(input("Enter second number: "))

output = float(operation[input_operation](n1, n2))
print(output)

keep_calc = input("Do you want to keep calculating with the same number(y) or no (n): ")
while keep_calc == "y":
    input_operation = input("Enter operation: ")
    n2 = int(input("Enter second number: "))
    output = float(operation[input_operation](output, n2))
    print(output)
    keep_calc = input("Do you want to keep calculating with the same number(y) or no(n): ")

print("Thank you!")