tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    print("#%d" % t)
    for y in range(n):
        for x in range(n):
            print(arr[n - x - 1][y], end="")
        print(" ", end="")
        for w in range(n):
            print(arr[n - y - 1][n - w - 1], end="")
        print(" ", end="")
        for z in range(n):
            print(arr[z][n - y - 1], end="")
        print()
