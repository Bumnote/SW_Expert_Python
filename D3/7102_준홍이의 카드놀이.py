tc = int(input())

for t in range(1, tc + 1):
    n, m = map(int, input().split())
    count = [0] * (n + m + 1)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            count[i + j] += 1

    print("#%d" % t, end=" ")
    for i in range(2,n+m+1):
        if count[i] == max(count):
            print(i, end=" ")
