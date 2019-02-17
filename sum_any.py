def digit_sum():
    sum = 0
    for each in range(0, num):
        n = input("Enter a integer")
        _num = int(n)
        sum += _num
    print("The sum of integers is {}".format(sum))


x = input("Enter how many numbers to enter:")
num = int(x)
digit_sum()

