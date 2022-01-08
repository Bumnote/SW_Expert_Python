tc = int(input())

for t in range(1, tc + 1):
    day, hour, minute = map(int, input().split())
    # 2011년 11월 11일 오전 11시 11분
    answer = (day * 24 * 60 + hour * 60 + minute) - (24 * 11 * 60 + 11 * 60 + 11)
    if answer < 0:
        print("#%d %d" % (t, -1))
    else:
        print("#%d %d" % (t, answer))
