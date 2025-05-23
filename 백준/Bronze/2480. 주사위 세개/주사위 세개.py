lst = list(map(int, input().split()))
lst.sort()
if lst[0] == lst[1] and lst[1] == lst[2]:
    result = 10000+lst[0]*1000
elif lst[0] == lst[1] or lst[1] == lst[2]:
    result = 1000 + lst[1] * 100
else:
    result = lst[2] * 100
print(result)