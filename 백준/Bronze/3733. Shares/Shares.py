while True:
    try:
        N, x = map(int, input().split())
        print(x//(N+1))
    except EOFError:
        break