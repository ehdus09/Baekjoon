import itertools
number = [int(input()) for _ in range(9)]
total = itertools.combinations(number, 7)
for i in total:
    if sum(i) == 100:
        result = sorted(i)
        for j in result:
            print(j)
        break