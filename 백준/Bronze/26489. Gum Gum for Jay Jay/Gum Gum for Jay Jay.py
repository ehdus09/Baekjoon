cnt = 0
while True:
    try:
        sen = input()
        cnt += 1
    except EOFError:
        print(cnt)
        break