n, m = map(int, input().split())
basket = [0 for _ in range(n)]
for i in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):
        basket[idx] = k
for i in basket:
    print(i, end=" ")