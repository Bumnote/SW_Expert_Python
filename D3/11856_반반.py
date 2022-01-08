tc = int(input())

for t in range(1, tc + 1):
    s = list(input())
    arr = set(s)
    if len(arr) == 2:
        print("#%d %s" % (t, "Yes"))
    else:
        print("#%d %s" % (t, "No"))
