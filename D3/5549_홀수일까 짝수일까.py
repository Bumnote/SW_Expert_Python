tc = int(input())

for t in range(1, tc + 1):
    s = input()
    number = int(s[-1])
    answer = "Odd"
    if number % 2 == 0:
        answer = "Even"

    print("#%d %s" % (t, answer))
