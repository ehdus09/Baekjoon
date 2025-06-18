t = int(input())
for i in range(t):
    sen = input().split()
    for j in sen:
        print(j[::-1], end=" ")