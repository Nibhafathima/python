lst=[]
lst2=[]
n=int(input("enter the limit of  element:"))
for i in range(0,n):
    x=int(input("enter the element in list:"))
    lst.append(x)
for num in lst:
    if num>0:
        lst2.append(num)
    
print("orginal list:",lst)
print("list with postive integers:",lst2)
