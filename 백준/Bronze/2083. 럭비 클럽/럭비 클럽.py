while True:
    name, age, weight = input().split()
    if name == "#":
        break
    else:
        if int(age) > 17 or int(weight) >= 80:
            result = "Senior"
        else:
            result = "Junior"
    print(f'{name} {result}')