N = int(input())
lst = list(map(int, input().split()))
maxNum = lst[0]
minNum = lst[0]
for i in lst[1:]:
    if maxNum < i:
        maxNum = i
    elif minNum > i:
        minNum = i
    
print(minNum, maxNum)