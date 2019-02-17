list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list1 = [x for (i,x) in enumerate(list1) if i not in (0,4,5)]
print(list1)