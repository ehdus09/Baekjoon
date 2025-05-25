while True:
    n = int(input())
    hap = 0
    if n == 0:
        break
    else:
        for i in range(n):
            hap += (n-i)
        print(hap)