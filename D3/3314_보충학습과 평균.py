tc = int(input())

for t in range(1, tc + 1):
    Sum = 0
    arr = list(map(int, input().split()))
    for i in arr:
        if i < 40:
            Sum += 40
        else:
            Sum += i
    avg = Sum // 5
    print("#%d %d" % (t, avg))
