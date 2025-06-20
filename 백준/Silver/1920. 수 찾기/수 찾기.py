n = int(input())
arr = set(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

for i in nums:
    print(1 if i in arr else 0)