a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180:
    if a == b and b == c and c == a:
        result = "Equilateral"
    elif a == b or b == c or c == a:
        result = "Isosceles"
    elif a != b and b != c and c != a:
        result = "Scalene"
else:
    result = "Error"
print(result)