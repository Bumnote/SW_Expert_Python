tc = int(input())

for t in range(1, tc + 1):
    cnt = int(input())
    answer = []
    for i in range(cnt):
        number = int(input())
        if number == 0:
            answer.pop()
        else:
            answer.append(number)

    print("#%d %d" % (t, sum(answer)))
