sen = input().split("-")

# 첫 번째 덩어리는 무조건 더해줍니다
result = sum(map(int, sen[0].split("+")))

# 두 번째 덩어리부터는 괄호로 묶어서 모두 빼줍니다
for i in range(1, len(sen)):
    result -= sum(map(int, sen[i].split("+")))

print(result)