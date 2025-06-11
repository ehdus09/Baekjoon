n = int(input())
s = input().lower()
vowel = 'aeiou'
cnt = 0
for i in s:
    if i in vowel:
        cnt += 1
print(cnt)