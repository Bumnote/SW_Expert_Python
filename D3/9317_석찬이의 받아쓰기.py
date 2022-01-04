tc = int(input())

for t in range(1, tc + 1):
    length = int(input())
    s = list(input())
    temp = list(input())

    answer = 0
    for i in range(length):
        if s[i] == temp[i]:
            answer += 1

    print("#%d %d" % (t, answer))
