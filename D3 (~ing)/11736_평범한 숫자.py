tc = int(input())

for t in range(1, tc + 1):
    cnt = int(input())
    number = list(map(int, input().split()))
    answer = 0

    for i in range(1, len(number) - 1):
        if (number[i - 1] < number[i] < number[i + 1]) or number[i - 1] > number[i] > number[i + 1]:
            answer += 1

    print("#%d %d" % (t, answer))
