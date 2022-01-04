tc = int(input())

for t in range(1, tc + 1):
    number = set(list(input()))
    answer = len(number)

    print("#%d %d" % (t, answer))
