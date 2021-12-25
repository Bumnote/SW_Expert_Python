tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    arr = [[1] * i for i in range(1, n + 1)]

    for y in range(2, n):
        for x in range(y + 1):
            if x != 0 and x != y:
                arr[y][x] = arr[y - 1][x - 1] + arr[y - 1][x]

    print("#%d" % (t))
    for y in arr:
        for x in y:
            print(x, end=" ")
        print()
