tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    answer = 0
    p = [0, 1, 1, 1, 2, 2]
    if n <= 5:
        answer = p[n]
    else:
        for i in range(6, n + 1):
            p.append(p[i - 5] + p[i - 1])
        answer = p[n]

    print("#%d %d" % (t, answer))
