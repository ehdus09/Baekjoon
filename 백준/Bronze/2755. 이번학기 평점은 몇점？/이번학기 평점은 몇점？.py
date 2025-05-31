from decimal import Decimal, ROUND_HALF_UP
scores = {'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}
score = 0
totalhak = 0
n=int(input())
for i in range(n):
    subject, hakjum, grade = input().split()
    score+=int(hakjum)*scores[grade]
    totalhak += int(hakjum)
avg = Decimal(str(score / totalhak)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(avg)