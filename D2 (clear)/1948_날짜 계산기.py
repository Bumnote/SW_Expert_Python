tc = int(input())

for t in range(1, tc + 1):
    a_month, a_day, b_month, b_day = map(int, input().split())
    answer = 0
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    if a_month == b_month:
        answer = b_day - a_day + 1
        print("#%d %d" % (t, answer))
    else:
        answer = (day[a_month - 1] - a_day + 1) + b_day
        for i in range(a_month + 1, b_month):
            answer += day[i - 1]
        print("#%d %d" % (t, answer))
