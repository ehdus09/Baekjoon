n, m = map(int, input().split())
lst1 =[]
for i in range(n):
    nums = list(map(int, input().split()))
    lst1.append(nums)
lst2 =[]
for i in range(n):
    nums = list(map(int, input().split()))
    lst2.append(nums)
for i in range(n):
    for j in range(m):
        print(lst1[i][j]+lst2[i][j], end=" ")
    print()