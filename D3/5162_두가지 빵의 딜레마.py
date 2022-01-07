tc = int(input())

for t in range(1, tc + 1):
    a, b, c = map(int, input().split())

    answer = 0
    if a > b:
        answer = c // b + (c % b) // a
    else:
        answer = c // a + (c % a) // b

    print("#%d %d" % (t, answer))
