tc = int(input())

for t in range(1, tc + 1):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))

    Sum = 0
    Max = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            # 두 봉지의 무게의 최댓값을 구하기. (단, 최대 무게의 제한이 있다.)
            Sum += (weight[i] + weight[j])
            if Max <= Sum <= m:
                Max = Sum
            Sum = 0

    if Max == 0:
        print("#%d %d" % (t, -1))
    else:
        print("#%d %d" % (t, Max))
