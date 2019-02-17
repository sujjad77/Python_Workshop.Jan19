count_even=0
count_odd=0
_list1=[]
_list2=[]
for i in range(1,10):
    if(i%2==0):
        _list1.append(i)
    else:
          _list2.append(i)
    
print("Number of even numbers:",len(_list1))
print("Number of odd numbers:",len(_list2))
