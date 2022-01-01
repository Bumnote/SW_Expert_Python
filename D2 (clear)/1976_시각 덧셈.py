tc = int(input())

for t in range(1, tc + 1):
    hour_1, minute_1, hour_2, minute_2 = map(int, input().split())
    hour = hour_1 + hour_2 + (minute_1 + minute_2) // 60
    minute = (minute_1 + minute_2) % 60

    if hour >= 13:
        hour %= 12
        if hour == 0:
            hour = 12

    print("#%d %d %d" % (t, hour, minute))
