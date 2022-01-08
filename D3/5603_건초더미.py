tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    arr = []
    cnt = 0
    total = 0
    for _ in range(n):
        arr.append(int(input()))
        total += arr[-1]
    dumi = total // n
    arr.sort(reverse=True)
    for i in arr:
        if i > dumi:
            cnt += i - dumi
        else:
            break

    print("#%d %d" % (t, cnt))
