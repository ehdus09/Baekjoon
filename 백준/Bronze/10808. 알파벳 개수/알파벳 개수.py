t = input()
for i in range(26):
    cnt = t.count(chr(97+i))
    print(cnt, end=" ")