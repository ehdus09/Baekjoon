n, m = map(int, input().split())
money = n * 100
if money - m >= 0:
    print("Yes")
else:
    print("No")