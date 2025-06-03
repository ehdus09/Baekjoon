n = int(input())
hap = 0
three = 0
for i in range(1, n+1):
    hap += i
    three += i**3
print(hap)
print(hap ** 2)
print(three)