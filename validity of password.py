import re
validity= True
while validity:
    password=input("Enter a password:")

    if(len(password)<6 or len(password)>16):
        print("Invalid. Password must have total characters between 6 and 16")
        continue
    elif not re.search("[a-z]",password):
        print("Invalid. Password must contain one letter between [a-z]")
        continue
    elif not re.search("[A-Z]",password):
        print("Invalid. Password must contain one letter between [A-Z]")
        continue
    elif not re.search("[0-9]",password):
        print("Invalid. Password must contain one letter between [0-9]")
        continue
    elif not re.search("[@#$]",password):
        print("Invalid. Password must contain one letter between [@#$]")
        continue
    else:
        validity= False

if(validity):
    pass
else:
    print("Valid password")
