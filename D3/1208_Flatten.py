for t in range(1, 11):
    cnt = int(input())
    arr = list(map(int, input().split()))

    while cnt != 0:
        if max(arr) - min(arr) > 1:
            arr[arr.index(max(arr))] -= 1
            arr[arr.index(min(arr))] += 1
        else:
            print("#%d %d" % (t, max(arr) - min(arr)))
            break
        cnt -= 1
        if cnt == 0:
            print("#%d %d" % (t, max(arr) - min(arr)))
