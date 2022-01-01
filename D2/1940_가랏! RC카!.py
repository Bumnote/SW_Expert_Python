tc = int(input())

for t in range(1, tc + 1):
    cnt = int(input())
    distance = 0
    speed = 0
    command = []

    for _ in range(cnt):
        command = list(map(int, input().split()))
        # 가속하는 경우
        if command[0] == 1:
            speed += command[1]
        # 감속하는 경우
        elif command[0] == 2:
            # 현재 속도보다 감속 속도가 더 큰 경우, 속도는 0 --> 제약 조건
            if speed < command[1]:
                speed = 0
            else:
                speed -= command[1]

        # 계산된 속도만큼 이동거리 증가
        distance += speed

    print("#%d %d" % (t, distance))
