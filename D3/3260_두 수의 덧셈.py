tc = int(input())

for t in range(1, tc + 1):
    n, m = map(int, input().split())
    answer = n + m
    print("#%d %d" % (t, answer))
