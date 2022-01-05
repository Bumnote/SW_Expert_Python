tc = int(input())

for t in range(1, tc + 1):
    s = list(input().split())
    answer = ""
    for i in s:
        answer += i[0].upper()

    print("#%d %s" % (t, answer))
