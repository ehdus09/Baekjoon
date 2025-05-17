T = int(input())
for i in range(T):
    P = ""
    R, S = input().split()
    for i in S:
        P += i*int(R)
    print(P)