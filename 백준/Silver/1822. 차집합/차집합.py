na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
minus = sorted(a - b)
print(len(minus))
for i in minus:
    print(i, end=" ")