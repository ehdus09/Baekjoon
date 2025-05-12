t = input()
NewT = ""
for i in t:
    if i.isupper():
        NewT += i.lower()
    elif i.islower():
        NewT += i.upper()

print(NewT)