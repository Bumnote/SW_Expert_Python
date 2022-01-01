tc = int(input())

for t in range(1, tc + 1):
    # 초기 설정
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Sum = 0
    Max = 0
    # a의 길이가 더 긴 경우 Swap
    if a > b:
        a, b = b, a
        A, B = B, A

    for m in range(0, b - a + 1):
        for n in range(m, m + a):
            Sum += (A[n - m] * B[n])
        if Max < Sum:
            Max = Sum
        # Sum 초기화
        Sum = 0
    print("#%d %d" % (t, Max))
