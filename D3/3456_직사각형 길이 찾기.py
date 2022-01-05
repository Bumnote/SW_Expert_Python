tc = int(input())

for t in range(1, tc + 1):
    answer = 0
    length = list(map(int, input().split()))
    temp = list(set(length))
    if len(temp) == 1:
        answer = temp[0]
    else:
        for i in temp:
            if length.count(i) == 1:
                answer = i

    print("#%d %d" % (t, answer))
