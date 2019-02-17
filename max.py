def func(x,y,z):
    if(x>y and x>z):
        print("First number is max")
    elif(y>x and y>z):
        print("Second number is max")
    else:
        print("Third number is max")

x=input("Enter first number:")
y=input("Enter second number:")
z=input("Enter third number:")
func(x,y,z)
