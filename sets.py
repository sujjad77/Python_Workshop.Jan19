# sets

# update
set1 = {"Nepal", "Kathmandu", "Pokhara", "Dharan", "Chitwan"}
set1.update(( "Surkhet", "Everest"))
print(set1)

# intersection
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
s2 = {1, 2, 4, 6, 8}
print(s1.intersection(s2))
# defference
print(s1.difference(s2))
# union
print(s1.union(s2))
# subset and superset
print(s1.issuperset(s2))
print(s2.issubset(s1))
# clear
set1.clear()
print(set1)
# by spliting a string, we can add its elements to a set
strings= "This world is beautiful"

strr=strings.split(" ")
set3 = set(strr)
print(set3)