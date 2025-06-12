num = 1
while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    print(f'Case {num}: Sorting... done!')
    num += 1