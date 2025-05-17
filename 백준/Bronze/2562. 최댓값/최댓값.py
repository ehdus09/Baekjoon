maxNum = 0
cnt = 0
maxcnt = 0
for i in range(9):
    n = int(input())
    cnt += 1
    if n > maxNum:
        maxNum = n
        maxcnt = cnt
print(f'{maxNum}\n{maxcnt}')