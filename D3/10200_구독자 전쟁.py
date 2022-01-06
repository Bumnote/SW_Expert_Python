tc = int(input())

for t in range(1, tc + 1):
    n, a, b = map(int, input().split())
    Min_person = 0
    Max_person = 0

    if n < a + b:
        Min_person = a + b - n
        Max_person = a if a <= b else b
    else:
        Min_person = 0
        Max_person = a if a <= b else b

    print("#%d %d %d" % (t, Max_person, Min_person))
