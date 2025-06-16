n, m = map(int, input().split())
basket = [num for num in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    change = basket[i-1:j]
    change.reverse()
    basket[i-1:j] = change

for j in basket:
    print(j, end=" ")