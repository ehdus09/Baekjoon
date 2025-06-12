num = [int(input()) for _ in range(10)]
exceptNum = list(set(num))
count = {}
for i in exceptNum:
    count[i] = num.count(i)
print(f'{sum(num)/len(num):.0f}')
maxFrequency = max(count, key=count.get)
print(maxFrequency)