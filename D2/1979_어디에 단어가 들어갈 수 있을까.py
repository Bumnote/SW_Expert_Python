tc = int(input())

for t in range(1, tc + 1):
    n, k = map(int, input().split())

    arr = [list(map(int, input().split())) for i in range(n)]
    answer = 0
    cnt = 0

    # 가로 탐색
    for y in range(n):
        for x in range(n):
            if arr[y][x] == 1:
                cnt += 1
            else:
                if cnt == k:
                    answer += 1
                cnt = 0
        # 한 줄이 끝나면 검사하고 초기화
        if cnt == k:
            answer += 1
        cnt = 0
    # 세로 검사
    for y in range(n):
        for x in range(n):
            if arr[x][y] == 1:
                cnt += 1
            else:
                if cnt == k:
                    answer += 1
                cnt = 0
        if cnt == k:
            answer += 1
        cnt = 0

    print("#%d %d" % (t, answer))
