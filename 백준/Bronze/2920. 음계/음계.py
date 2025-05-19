n = list(map(int, input().split()))
asc = list(range(1, 9))
des = list(range(8, 0, -1))

if n == asc:
    print("ascending")
elif n == des:
    print("descending")
else:
    print("mixed")