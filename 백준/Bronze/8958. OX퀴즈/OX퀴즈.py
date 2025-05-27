n = int(input())
for i in range(n):
    rst = 0
    tc = input()
    num = 0
    for j in tc:
        if j == 'O':
            num += 1
            rst += num
        else:
            num = 0
    print(rst)