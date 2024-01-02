x=input("enter the string:")
if x.endswith ('ing'):
    y=x[-3:]+'ly'
    print(y)
else:
    print(x+'ing')
