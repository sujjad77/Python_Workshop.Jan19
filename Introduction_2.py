list=[1,2,3,4,5]
print(list*5)

#tuple
#tup = ()
#tup= tuple()
#r
x=1,2,3,4,5
print(x[0])
y=(1,)      #if single value has to be in a tuple then a comma after the element is required
print(y*6)
print(type(y))
t=(1,2,3,4,5)
print(2 in t)
t=t+(7,)
print(t)
g=1,2,3,4
print(g)
h,j,k,l=g #no of elements=no of assingning variables to unpack
print(j)

a=34
b=23
a,b=b,a
print(a)
print(b)

s={1,2,"sujan",(1,2,3)}
s.update(("Hello",2))
print(s)
print(type(s))
print(len(s))

d={
    "a": 34,
    "b":23
    }
print(d.keys())

print(d['a'])
print(d.get('b'))

print(hash("a")) #hash value is a unique no of a finite value, used only in immutable value
print(hash((1,2)))
print(hash("a"))
print(hash("a"))

list1=[0,1,2,3,4,5,6,7,8,9,10]
list2=[]

for i in list1:
    if i%2==0:
       list2.append(i)
print(list2)

#function
 
def sum(a,b):
    print(a+b)
sum(2,3)

def sum(a,b):
    return a+b
sum(2,3)

print(sum(2,3))

def _name(f="happy birthday to you"):

def sum_(*args):
    return sum_(args)
print(sum(1,2,3,4,4)
      
