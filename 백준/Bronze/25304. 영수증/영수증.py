x = int(input())
n = int(input())
hap = 0
for i in range(n):
    a, b = map(int, input().split())
    hap += a*b
if hap == x:
    print('Yes')
else:
    print('No')