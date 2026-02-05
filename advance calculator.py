import math

print("=== Advanced Calculator ===")

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square Root")
    print("7. Power")
    print("8. Sin")
    print("9. Cos")
    print("0. Exit")

    choice = input("Enter no of your operation: ")

    if choice == "0":
        print("Calculator band ho gaya 👍")
        break

    elif choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a + b)

    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a - b)

    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a * b)

    elif choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            print("Error: Division by zero")
        else:
            print("Result =", a / b)

    elif choice == "5":
        a = float(input("Enter number: "))
        print("Result =", a * a)

    elif choice == "6":
        a = float(input("Enter number: "))
        print("Result =", math.sqrt(a))

    elif choice == "7":
        a = float(input("Enter base: "))
        b = float(input("Enter power: "))
        print("Result =", a ** b)

    elif choice == "8":
        a = float(input("Enter angle in degrees: "))
        print("Result =", math.sin(math.radians(a)))

    elif choice == "9":
        a = float(input("Enter angle in degrees: "))
        print("Result =", math.cos(math.radians(a)))

    else:
        print("Galat choice 😅")