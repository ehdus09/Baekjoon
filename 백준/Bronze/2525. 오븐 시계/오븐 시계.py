h, m = map(int, input().split())
time = int(input())
h2 = time // 60
m2 = time % 60
rsth = h + h2
rstm = m + m2
if rstm >= 60:
    rstm -= 60
    rsth += 1

rsth %= 24
print(rsth, rstm)