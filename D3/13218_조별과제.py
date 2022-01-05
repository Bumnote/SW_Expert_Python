tc = int(input())

for t in range(1, tc + 1):
    person = int(input())

    branch = person // 3
    print("#%d %d" % (t, branch))
