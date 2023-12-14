while True:
    print("*********************************************** ")
    print("*********************************************** ")
    print("*** Enter A if you want to Addition       : *** ")
    print("*** Enter D if you want to Division       : *** ")
    print("*** Enter M if you want to Multiplication : *** ")
    print("*** Enter S if you want to Subtraction    : *** ")
    print("*** Enter X if you want to Exit           : *** ")
    print("*********************************************** ")
    print("*********************************************** ")

    a=input("Please enter the letter corresponding to what you want to do: ").lower()

    if a=="x":
        break
    elif a== "a" or a=="d" or a=="m" or a=="s":
        if a=="a":
            b= float(input("Enter first number here  : "))
            c= float(input("Enter second number here : "))
            print(f"Result: {b+c} ")
        elif a=="d":
            b= float(input("Enter first number here  : "))
            c= float(input("Enter second number here : "))
            print(f"Result: {b/c} ")
        elif a=="m":
            b= float(input("Enter first number here  : "))
            c= float(input("Enter second number here : "))
            print(f"Result: {b*c} ")
        elif a=="s":
            b= float(input("Enter first number here  : "))
            c= float(input("Enter second number here : "))
            print(f"Result: {b-c} ")
        elif a=="x":
            break       
    else:
        print ("You have not chosen the correct option for what you want to do!!!")
    


    