tc = int(input())

for t in range(1, tc + 1):
    arr = list(map(int, input().split()))
    answer = sum(arr) / len(arr)

    print("#%d %d" % (t, round(answer)))
