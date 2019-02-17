def fact(num):
    if num < 0:
         print("No factorial exist")
    else:
        x = num
        for each in range(1, num):
            x = x*each
    print("The factorial of {} is {}".format(num, x))


a = input("Enter a number:")
num = int(a)
fact(num)


