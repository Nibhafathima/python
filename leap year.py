x=int(input("enter the current year:"))
y=int(input("enter the final year:"))
for i in range(x,y+1):
    if i%4 == 0 or i%100 != 0 and i%400 == 0 :
        print(i,"year is leap year")