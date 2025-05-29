def fact(a):
    if a < 2:
        return 1
    else:
        return a * fact(a-1)

#main
n = int(input())
print(fact(n))