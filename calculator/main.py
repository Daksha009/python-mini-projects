try:
    a = int(input("Enter the first number: "))

    b = int(input("Enter the second number: "))

    print("What kind of operation you wanna perform.Press + for addition\nPress - for subtraction\nPress * for multiplication\nPress / for division")

    o = input("Enter the operation: ")
    match o:
        case "+":
            print(f"The result is :{a+b}")
        case "-":
            print(f"The result is :{a-b}")
        case "*":
            print(f"The result is :{a*b}")
        case "/":
            print(f"The result is :{a/b}")
        case default:
            print("Invalid operation. Please enter +, -, *, or /.")
                

except Exception as e:
    print("Enter a valid value of a and b")    