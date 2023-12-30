lst=[]
n=int(input("enter the limit:"))
for i in range(0,n):
    x=int(input("enter the elemnt:"))
    lst.append(x)
for num in lst:
    if num%2==0:
        lst.remove(num)
print(lst)
