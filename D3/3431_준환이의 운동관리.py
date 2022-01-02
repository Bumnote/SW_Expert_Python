tc = int(input())

for t in range(1, tc + 1):
    l, u, x = map(int, input().split())

    if x < l:
        print("#%d %d" % (t, l - x))
    elif l <= x <= u:
        print("#%d %d" % (t, 0))
    else:
        print("#%d %d" % (t, -1))
