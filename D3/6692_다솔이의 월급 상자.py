tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    answer = 0
    for i in range(n):
        a, b = input().split()
        answer += float(a) * int(b)

    print("#%d %f" % (t, answer))
