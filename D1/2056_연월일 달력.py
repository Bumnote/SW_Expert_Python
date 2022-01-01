tc = int(input())

for t in range(1, tc + 1):
    daily = int(input())
    year = daily // 10000
    daily %= 10000
    month = daily // 100
    daily %= 100
    day = daily

    if year >= 0 and (1 <= month <= 12):
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (
                1 <= day <= 31):
            print("#%d %04d/%02d/%02d" % (t, year, month, day))
        elif (month == 4 or month == 6 or month == 9 or month == 11) and (1 <= day <= 30):
            print("#%d %04d/%02d/%02d" % (t, year, month, day))
        elif month == 2 and (1 <= day <= 28):
            print("#%d %04d/%02d/%02d" % (t, year, month, day))
        else:
            print("#%d %d" % (t, -1))
    else:
        print("#%d %d" % (t, -1))
