tc = int(input())

for t in range(1, tc + 1):
    first_hour, second_hour = map(int, input().split())
    hour = (first_hour + second_hour) % 24

    print("#%d %d" % (t, hour))
