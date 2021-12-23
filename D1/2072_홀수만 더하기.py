tc = int(input())

for t in range(1, tc + 1):
    arr = list(map(int, input().split()))
    answer = 0
    for i in arr:
        if i % 2 == 1:
            answer += i
    print("#%d %d" % (t, answer))
