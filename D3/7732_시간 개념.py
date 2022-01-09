tc = int(input())

for t in range(1, tc + 1):
    current = list(map(int, input().split(":")))
    promise = list(map(int, input().split(":")))
    current_sec = current[0] * 60 * 60 + current[1] * 60 + current[2]
    promise_sec = promise[0] * 60 * 60 + promise[1] * 60 + promise[2]

    # 시간을 모두 초로 변환한 후에 생각하자.
    if current_sec < promise_sec:
        time = promise_sec - current_sec
        hour = time // 3600
        time %= 3600
        minute = time // 60
        second = time % 60
        print("#%d %02d:%02d:%02d" % (t, hour, minute, second))
    else:
        promise_sec += 24 * 60 * 60
        time = promise_sec - current_sec
        hour = time // 3600
        time %= 3600
        minute = time // 60
        second = time % 60
        print("#%d %02d:%02d:%02d" % (t, hour, minute, second))
