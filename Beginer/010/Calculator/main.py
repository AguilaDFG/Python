from art import logo
def add(n1,n2):
    return n1 + n2
def substract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
operations = {"+": add, "-": substract, "*": multiply, "/": divide}
def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    repeat = True
    while repeat:
        for a in operations:
            print(a)
        symbol = input("Choose an operatioin from above: ")
        num2 = float(input("What's the next number? "))
        result = operations[symbol](num1, num2)
        print (f"{num1} {symbol} {num2} = {result}")
        repeat_q = input(f"Do you want to continue with first number: {num1}? Type 'y' or 'n': ").lower()
        if repeat_q == "y":
            num1 = result
        else:
            repeat = False
            calculator()
calculator()