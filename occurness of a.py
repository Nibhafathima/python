
l1=[input("enter the element: ")for i in range(int(input("enter the limit: ")))]
print('the list is: ',l1)

n=input("enter the word to count: ")
c=sum(i.count(n) for i in l1)
print("occurness of count of a in list : ",c)
