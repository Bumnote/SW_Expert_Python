for t in range(1, 11):
    test_case = int(input())
    number = [list(map(int, input().split())) for _ in range(100)]

    Max = 0
    Sum_x = 0  # 행의 합
    Sum_y = 0  # 열의 합
    Sum_z = 0  # 우 대각선의 합
    Sum_w = 0  # 좌 대각선의 합
    for y in range(100):
        for x in range(100):
            Sum_x += number[y][x]
            Sum_y += number[x][y]
        Sum_z += number[y][y]
        Sum_w += number[y][99 - y]
        if Max < Sum_x:
            Max = Sum_x
        if Max < Sum_y:
            Max = Sum_y
        Sum_x = 0
        Sum_y = 0
    if Max < Sum_z:
        Max = Sum_z
    if Max < Sum_w:
        Max = Sum_w

    print("#%d %d" % (test_case, Max))
