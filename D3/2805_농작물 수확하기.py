tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    crop = [list(input()) for _ in range(n)]
    Sum = 0  # 문제에 해당하는 값들의 합 변수
    flag = 0 # 범위를 변경시키라는 신호를 주는 변수
    for y in range(n):
        if flag == 0:
            for x in range((n // 2) - y, (n // 2) + 1 + y):
                Sum += int(crop[y][x])
            if y == n // 2:
                flag += 1
        else:
            for x in range(flag, n - flag):
                Sum += int(crop[y][x])
            flag += 1

    print("#%d %d" % (t, Sum))
