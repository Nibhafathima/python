colour=[]
n=int(input("enter the number of color in list: "))
for i in range(0,n):
    c=input("enter the colour: ")
    colour.append(c)
print(colour)
first_colour=colour[0]
last_colour=colour[n-1]
print("first colour: ",first_colour)
print("last colour: ",last_colour)


