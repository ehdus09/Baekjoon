word = [input() for i in range(5)]

maxLen = max(len(i) for i in word)

for i in range(maxLen):
    for j in range(len(word)):
        if i < len(word[j]):
            print(word[j][i], end="")