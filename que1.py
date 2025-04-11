def integers():
    while True:
        try:
            num1=int(input("Enter a first number: "))
            num2=int(input("Enter a second number: "))
            division=num1/num2
            print(f"The division of two number is {division}")
        except  ValueError:
            print("please enter integer only")
        except ZeroDivisionError:
            print("Please enter number except 0")
        
integers()


