hambugers = []
drinks = []
for i in range(3):
    hambuger = int(input())
    hambugers.append(hambuger)
for i in range(2):
    drink = int(input())
    drinks.append(drink)
print(min(hambugers)+min(drinks)-50)