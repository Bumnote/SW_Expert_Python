tc = int(input())

for t in range(1, tc + 1):
    a, b = map(int, input().split())

    if a >= 10 or b >= 10:
        print("#%d %d" % (t, -1))
    else:
        print("#%d %d" % (t, a * b))
