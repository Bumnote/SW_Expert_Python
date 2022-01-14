tc = int(input())

for t in range(1, tc + 1):
    n, k = map(int, input().split())  # n명 / k조
    Sum = 0
    i = 1
    j = 0
    for p in range(1, n + 1):
        if p % 2 == 1:
            Sum += i
            i += 2 * k
        else:
            j += 2 * k
            Sum += j

    print("#%d" % t, end=" ")
    # 조 인원이 짝수인 경우
    if n % 2 == 0:
        for _ in range(k):
            print(Sum, end=" ")
    # 조 인원이 홀수인 경우
    else:
        for _ in range(k):
            print(Sum, end=" ")
            Sum += 1
