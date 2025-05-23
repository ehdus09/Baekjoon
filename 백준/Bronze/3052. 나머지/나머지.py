lst = []
for i in range(10):
    n = int(input())
    reminder = n % 42
    if reminder not in lst:
        lst.append(reminder)

print(len(lst))