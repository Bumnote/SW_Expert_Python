tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    arr = [[0] * n for i in range(n)]

    value = 1
    x = 0
    y = 0
    flag = 0
    for _ in range(n):
        for _ in range(n):
            arr[y][x] = value
            if (0 <= y + dy[flag % 4] < n) and (0 <= x + dx[flag % 4] < n) and (arr[y + dy[flag % 4]][x + dx[flag % 4]] == 0):
                value += 1
                y += dy[flag % 4]
                x += dx[flag % 4]
            else:
                value += 1
                flag += 1
                y += dy[flag % 4]
                x += dx[flag % 4]

    # 정답 출력
    print("#%d" % t)
    for y in range(n):
        for x in range(n):
            print(arr[y][x], end=" ")
        print()
