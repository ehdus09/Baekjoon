t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    room = n // h + 1
    if floor == 0:
        floor = h
        room = n // h
    print(f'{floor}{room:02}')