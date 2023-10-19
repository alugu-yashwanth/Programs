x=9
while(x<15):
    print(x, "While loop is working")
    x=x+2

print("While loop closed")

# now there is no do-while loop in python so we can perform a do-while loop by using a infinite loop and using a break condition
# let say a program for positive numbers
while(True):
    x=int(input("Enter a number: "))
    print(x)
    if x<0:
        break
