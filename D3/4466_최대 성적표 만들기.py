tc = int(input())

for t in range(1, tc + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    answer = 0
    for i in range(k):
        answer += arr[i]

    print("#%d %d" % (t, answer))
