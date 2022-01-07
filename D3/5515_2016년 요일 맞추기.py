tc = int(input())
# 2016년 1월 1일 --> 금요일
#  0  1  2  3  4  5  6
# 월 화 수  목 금 토 일
for t in range(1, tc + 1):
    month, day = map(int, input().split())
    total_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 1월 1일은 금요일이기 때문에 4부터 배열 시작
    everyday = [4, 5, 6, 0, 1, 2, 3]
    # 1월 1일에서 입력받은 날짜까지의 일 수를 구한다.
    between = 0
    if month == 1:
        between += day - 1
    else:
        between += total_day[0] + day - 1
        for i in range(1, month - 1):
            between += total_day[i]

    answer = everyday[between % 7]
    print("#%d %d" % (t, answer))
