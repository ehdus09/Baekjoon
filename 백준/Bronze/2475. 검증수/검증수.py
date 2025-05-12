a, b, c, d, e = map(int, input().split())
hap = 0
for i in a, b, c, d, e:
    i **= 2
    hap += i
print(hap%10)