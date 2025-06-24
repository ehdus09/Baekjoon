scores = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

score = 0
totalhak = 0

while True:
    try:
        subject, hakjum, grade = input().split()
        if grade == "P":
            continue
        hakjum = float(hakjum)
        score+= hakjum * scores[grade]
        totalhak += hakjum
    except EOFError:
        break

avg = score/totalhak
print(avg)