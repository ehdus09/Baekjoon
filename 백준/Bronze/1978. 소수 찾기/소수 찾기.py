n = int(input())
num = map(int, input().split())
cnt = 0
for i in num:
    yaksu = 0
    for j in range(1, i+1):
        if i % j == 0:
            yaksu += 1
    if yaksu == 2:
        cnt += 1
print(cnt)