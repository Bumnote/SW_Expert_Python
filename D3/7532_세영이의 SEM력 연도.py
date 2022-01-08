tc = int(input())

for t in range(1, tc + 1):
    s, e, m = map(int, input().split())
    # 1 <= s <= 365
    # 1 <= e <= 24
    # 1 <= m <= 29
    answer = 0
    while True:
        if s == 1 and e == 1 and m == 1:
            answer += 1
            break
        s -= 1
        e -= 1
        m -= 1
        answer += 1
        if s == 0:
            s = 365
        if e == 0:
            e = 24
        if m == 0:
            m = 29

    print("#%d %d" % (t, answer))
