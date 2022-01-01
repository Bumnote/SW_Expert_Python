tc = int(input())

for t in range(1, tc + 1):
    cnt = int(input())
    arr = list(map(int, input().split()))

    for i in range(cnt):
        arr[i] = arr[i] - 0 if arr[i] > 0 else 0 - arr[i]

    print("#%d %d %d" % (t, min(arr), arr.count(min(arr))))
