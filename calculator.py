a = int(input("Enter the value for a: "))

b = int(input("Enter the value for b: "))

operation = input("Choose math operation (+, -, x, :): ")

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "x":
    print(a * b)
elif operation == ":":
    print(a / b)
else:
    print("Math operation is't corret")

