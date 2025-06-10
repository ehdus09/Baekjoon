price = [int(input()) for _ in range(10)]
total = max(price)
price.remove(total)
rest = sum(price)
print(total - rest)