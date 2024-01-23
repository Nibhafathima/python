l1=[]
x=int(input("enter the limit of the list: "))
for i in range(x):
    y=input('enter the element: ')
    l1.append(y)

l2=[]
z=int(input("enter the limit of the list2: "))
for i in range(z):
    w=input('enter the element: ')
    l2.append(w)
print(l1)
print(l2)



if len(l1) == len(l2):
    print("both list have same length ")
else:
    print("both have different length")
l1=list(map(int,l1))
l2=list(map(int,(l2)))
if sum(l1) == sum(l2):
    print("both have same sum")
else:
    print("both have diffrent sum")
    
common_words=list(set(l1)&set(l2))
    
print("common words in both list: ",common_words)


