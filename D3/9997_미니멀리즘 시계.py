tc = int(input())

for t in range(1, tc + 1):
    degree = int(input()) * 2
    hour = degree // 60
    hour %= 12
    minute = degree % 60

    print("#%d %d %d" % (t, hour, minute))
