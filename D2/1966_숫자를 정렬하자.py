tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    print("#%d" % t, end=" ")
    for i in arr:
        print(i, end=" ")
    print()
