tc = int(input())

for t in range(1, tc + 1):
    # 스도쿠 담기 --> list comprehension
    square = [list(map(int, input().split())) for _ in range(9)]
    # 스도쿠 검사할 cnt 리스트
    cnt = [0] * 9
    stop_sign = 0
    # 가로 검사
    for i in square:
        for j in i:
            cnt[j % 9] += 1
        # cnt의 모든 값이 1이 아니라면 스도쿠 탈락
        if cnt.count(1) != 9:
            print("#%d %d" % (t, 0))
            stop_sign += 1
            break
        # cnt의 모든 값이 1이라면 다시 cnt 초기화
        else:
            cnt = [0] * 9
    # stop_sign이 0이 아니라면 다음 테스트 케이스로 진행
    if stop_sign != 0:
        continue

    # 세로 검사
    for i in range(9):
        for j in range(9):
            cnt[square[j][i] % 9] += 1
        # cnt의 모든 값이 1이 아니라면 스도쿠 탈락
        if cnt.count(1) != 9:
            print("#%d %d" % (t, 0))
            stop_sign += 1
            break
        # cnt의 모든 값이 1이라면 다시 cnt 초기화
        else:
            cnt = [0] * 9
    # stop_sign이 0 이 아니라면 다음 테스트 케이스로 진행
    if stop_sign != 0:
        continue

    # 네모 검사
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            for dy in range(3):
                for dx in range(3):
                    # y , x의 0, 3, 6 번째 위치에서 3 x 3 스도쿠 검사
                    cnt[square[y + dy][x + dx] % 9] += 1
            # cnt의 모든 값이 1이 아니라면 스도쿠 탈락
            if cnt.count(1) != 9:
                stop_sign += 1
                break
            # cnt의 모든 값이 1이라면 다시 cnt 초기화
            else:
                cnt = [0] * 9
        if stop_sign != 0:
            break

    if stop_sign != 0:
        print("#%d %d" % (t, 0))
    else:
        print("#%d %d" % (t, 1))
