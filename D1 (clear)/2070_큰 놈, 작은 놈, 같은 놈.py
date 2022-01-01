tc = int(input())

for t in range(1, tc + 1):
    a, b = map(int, input().split())
    if a < b:
        print("#%d %s" % (t, "<"))
    elif a > b:
        print("#%d %s" % (t, ">"))
    else:
        print("#%d %s" % (t, "="))
