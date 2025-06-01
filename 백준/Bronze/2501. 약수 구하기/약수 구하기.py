n, k = map(int, input().split())
yaksu = []
for i in range(1,n+1):
    if n % i == 0:
        yaksu.append(i)
yaksu.sort()

try:
    print(yaksu[k-1])
except IndexError:
    print(0)