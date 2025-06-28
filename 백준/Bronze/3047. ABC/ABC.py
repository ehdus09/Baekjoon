num = list(map(int, input().split()))
num.sort()
nums = {"A":num[0], "B":num[1], "C":num[2]}
sequence = input()
for i in sequence:
    print(nums[i], end=" ")