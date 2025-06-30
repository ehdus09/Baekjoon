import math
numerator1, denominator1 = map(int, input().split())
numerator2, denominator2 = map(int, input().split())

common = math.lcm(denominator1, denominator2)

numeHap = numerator1*(common//denominator1) + numerator2*(common//denominator2)

gcd = math.gcd(numeHap, common)
numeHap //= gcd
common //= gcd

print(numeHap, common)