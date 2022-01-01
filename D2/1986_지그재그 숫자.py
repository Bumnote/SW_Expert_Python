tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    answer = 0

    for i in range(1, n + 1):
        if i % 2 == 1:
            answer += i
        else:
            answer -= i

    print("#%d %d" % (t, answer))
