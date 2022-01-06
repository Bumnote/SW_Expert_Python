tc = int(input())

for t in range(1, tc + 1):
    s = input().strip()
    arr = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    answer = 6 - arr.index(s)
    if answer == 0:
        answer = 7

    print("#%d %d" % (t, answer))
