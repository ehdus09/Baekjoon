import math
import itertools

t = int(input())
for i in range(t):
    num = list(map(int, input().split()))
    gcd = []
    for a, b in itertools.combinations(num, 2):
        gcd.append(math.gcd(a, b))
    print(max(gcd))