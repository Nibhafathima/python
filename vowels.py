v=[]
x=input("enter the word:")
v.append(x)
vow=[]
for char in x:
    if char.lower()in "aeiou" or char.upper()in "AEIOU":
        vow.append(char)
print("word:",v)
print("vowels in the words:",vow)
