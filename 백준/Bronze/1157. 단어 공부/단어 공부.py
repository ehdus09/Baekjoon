word = input().upper()
checked = []
cnt = {}
for i in word:
    if i not in checked:
        cnt[i] = word.count(i)
        checked.append(i)
maxCount = max(cnt.values())
maxAlpha = [i for i in cnt if cnt[i] == maxCount ]
if len(maxAlpha) > 1:
    print("?")
else:
    print(maxAlpha[0])