_dog_age= input("Enter dog's age in human's years:")
dog_age=int(_dog_age)

if (dog_age <= 2):
    age = dog_age * 10.5
    print("The age of dog in dog's years is {}".format(age))
else:
    age=(2*10.5)+((dog_age-2)*4)
    print("The dog's age in dog's years is {}".format(age))
