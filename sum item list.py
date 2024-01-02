l=[]
n=int(input("enter the limit: "))
for i in range(0,n):
    num=int(input("enter the number: "))
    l.append(num)
sum_list=sum(l)
print("THE LIST: ",l)
print("sum of list is: ",sum_list)
