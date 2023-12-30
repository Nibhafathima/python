dict1={}
n=int(input("enter the limit of dict: "))
for i in range(0,n):
    k=int(input("enter the key: "))
    v=input("enter the value: ")
    dict1[k]=[v]
assending=sorted(dict1.items())
descending=sorted(dict1.items(),reverse=True)
print("the dict: ",dict1)
print("ascending order: ",assending)
print("descending order: ",descending)


