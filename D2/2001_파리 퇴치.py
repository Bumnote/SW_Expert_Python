tc = int(input())

for t in range(1, tc + 1):
    # 기본 셋팅
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(n)]

    answer = 0
    Sum = 0
    # n x n 배열에서 m x m 배열을 탐색
    for y in range(n - m + 1):
        for x in range(n - m + 1):
            # 해당 위치에서 m x m 배열을 탐색
            for z in range(m):
                for w in range(m):
                    Sum += arr[y + z][x + w]
            if answer < Sum:
                answer = Sum
            Sum = 0

    print("#%d %d" % (t, answer))
