tc = int(input())

for t in range(1, tc + 1):
    s = input()
    answer = ""
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'q':
            answer += 'p'
        elif s[i] == 'p':
            answer += 'q'
        elif s[i] == 'b':
            answer += 'd'
        else:
            answer += 'b'

    print("#%d %s" % (t, answer))
