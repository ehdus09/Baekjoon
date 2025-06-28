import math
import itertools

t = int(input())
for i in range(t):
    num = list(map(int, input().split()))
    n = num[0]
    nums = num[1:]

    total = 0
    for a, b in itertools.combinations(nums, 2):
        total += math.gcd(a, b)

    print(total)
