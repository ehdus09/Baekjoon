def sort(word):
    return (len(word), word)

# main
n = int(input())
word = list(set([input() for i in range(n)]))
sortWord = sorted(word, key=sort)
for i in sortWord:
    print(i)