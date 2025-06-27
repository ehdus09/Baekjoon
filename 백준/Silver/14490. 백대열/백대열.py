import math
n,m = map(int, input().split(":"))
yakbun = math.gcd(n, m)
print(f"{n//yakbun}:{m//yakbun}")