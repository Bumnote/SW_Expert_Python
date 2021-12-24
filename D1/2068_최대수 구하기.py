tc = int(input())

for t in range(1, tc + 1):
    arr = list(map(int, input().split()))

    print("#%d %d" % (t, max(arr)))
