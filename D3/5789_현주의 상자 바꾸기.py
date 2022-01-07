tc = int(input())

for t in range(1, tc + 1):
    # n개의 상자 --> 모두 0으로 적혀있다. / q회
    n, q = map(int, input().split())
    arr = [0] * n
    for cnt in range(1, q + 1):
        l, r = map(int, input().split())
        for i in range(l - 1, r):
            arr[i] = cnt

    print("#%d" % t, end=" ")
    for i in arr:
        print(i, end=" ")
    print()
