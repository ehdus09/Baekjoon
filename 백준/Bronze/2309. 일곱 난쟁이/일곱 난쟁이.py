import itertools
height = [int(input()) for _ in range(9)]
combin = itertools.combinations(height, 7)
for i in combin:
    if sum(i) == 100:
        result = sorted(i)
        for j in result:
            print(j)
        break