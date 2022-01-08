tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    flag = 0
    for i in range(1, 10):
        if n % i == 0 and (1 <= n // i <= 9):
            flag += 1
            print("#%d %s" % (t, "Yes"))
            break

    if flag == 0:
        print("#%d %s" % (t, "No"))
