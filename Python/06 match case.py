x=int(input("Enter the value of x:"))
match x:
    case 0:
        print("number is zero")
    case 2:
        print("number is two")
    case 4:
        print("number is four")
    case _ if x!=20:
        print("number is not equal to 20")
    case _ if x!=40:
        print("number is not equal to 40")
    case _:
        print(x)
