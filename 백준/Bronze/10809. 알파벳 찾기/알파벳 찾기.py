s = input()
for i in range(26):
    alpha = chr(97+i)
    if alpha in s:
        print(s.index(alpha), end=" ")
    else:
        print(-1, end=" ")