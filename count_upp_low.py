word=input("Enter a string:")
count1 = 0
count2 = 0
for i in word:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1


print("No. of lowercase characters is:{}".format(count1))
print("No. of uppercase characters is:{}".format(count2))
