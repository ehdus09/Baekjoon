n = int(input())
score = list(map(int, input().split()))
newScore = []
high = max(score)
for i in score:
    newScore.append(i/high*100)
print(sum(newScore)/len(newScore))