while True:
    try:
        n = int(input())
        hap = 0
        for i in range(n):
            hap += int(input())
        if hap == 0:
            print(0)
        elif hap > 0:
            print("+")
        else:
            print("-")
    except EOFError:
        break