import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2




should_continue = True
while should_continue:
    choose = input("what kind of operation you want it do?\n 1.add = + \n 2.subtract = - \n 3.multiply = * \n 4.divide = /\n").lower()
    number1 = int(input("What is your first number?: "))
    number2 = int(input("What is your second number?: "))
    if choose == "1":
        result = (add(number1, number2))
        print(f"this is your result: {result}")
    elif choose == "2":
        result = subtract(number1, number2)
        print(f"this is your result: {result}")
    elif choose == "3":
        result = multiply(number1, number2)
        print(f"this is your result: {result}")
    elif choose == "4":
        result = divide(number1, number2)
        print(f"this is your result: {result}")

    ok_or_no = input("would you like to continue or stop: ")
    if ok_or_no == "stop":
        should_continue = False

