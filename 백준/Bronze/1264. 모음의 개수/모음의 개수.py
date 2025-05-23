while True:
    cnt = 0
    t = input()
    if t == "#":
        break
    else:
        t = t.lower()
        cnt += t.count("a")
        cnt += t.count("e")
        cnt += t.count("i")
        cnt += t.count("o")
        cnt += t.count("u")
        print(cnt)