l=[]
n=int(input("enter the limit:"))
for i in range(0,n):
      num=int(input("enter the number:"))
      l.append(num)
square=[]
for num in l:
    square.append(num**2)
print(l)
print(square)
