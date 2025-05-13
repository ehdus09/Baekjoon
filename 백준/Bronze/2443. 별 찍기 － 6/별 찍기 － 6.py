n = int(input())
num=1
for i in range(1, n+1):
    for j in range(i-1):
        print(' ', end="")
    for k in range(n*2-num):
        print('*', end="")
    print()
    num += 2