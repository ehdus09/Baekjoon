from decimal import Decimal, ROUND_HALF_UP

n = int(input())

if n == 0:
    print(0)
else:
    difficulty = sorted([int(input()) for _ in range(n)])
    
    # 위, 아래에서 제외할 사람 수 계산 (반올림)
    cut = int(Decimal(n * 0.15).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    
    # 절사된 리스트 생성
    exception = difficulty[cut:n - cut]
    
    # 평균 계산
    avg = sum(exception) / len(exception)
    
    # 소수점 반올림 후 출력
    final = int(Decimal(avg).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    print(final)