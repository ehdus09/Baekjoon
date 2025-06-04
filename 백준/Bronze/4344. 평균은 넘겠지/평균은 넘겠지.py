c = int(input())
for tc in range(c):
    cnt = 0
    scores = list(map(int, input().split()))
    scores.remove(len(scores)-1)
    avg = sum(scores)/len(scores)
    for stu in scores:
        if stu > avg:
            cnt += 1
    print(f'{cnt/len(scores)*100:.3f}%')