tc = int(input())

for t in range(1, tc + 1):
    number = list(map(int, input().split()))
    Max = -1
    Min = 70
    for i in number:
        Sum = 0
        while i != 0:
            Sum += (i % 10)
            i //= 10
        if Max < Sum:
            Max = Sum
        if Min > Sum:
            Min = Sum

    print("#%d %d %d" % (t, Max, Min))
