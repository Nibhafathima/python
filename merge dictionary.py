d1={}
n=int(input("enter the limit of the dictionary: "))
for i in range(0,n):
    k=int(input("enter the key: "))
    v=(input("enter the value: "))
    d1[k]=[v]

d2={}
n=int(input("enter the limit of the dictionary: "))
for i in range(0,n):
    k2=int(input("enter the key: "))
    v2=(input("enter the value: "))
    d2[k2]=[v2]
d3={}
d3=d1|d2

print( "first dictionary: ",d1)
print( "second dictionary: ",d2)
print( "merge dictionary: ",d3)




