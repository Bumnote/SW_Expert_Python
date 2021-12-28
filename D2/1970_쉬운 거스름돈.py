tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    cnt = [0] * 8
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for i in range(len(money)):
        cnt[i] += (n // money[i])
        n %= money[i]

    print("#%d" % t)
    for i in cnt:
        print(i, end=" ")
    print()
