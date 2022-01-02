tc = int(input())

for t in range(1, tc + 1):
    s = input().strip()
    answer = ""
    for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            continue
        else:
            answer += i

    print("#%d %s" % (t, answer))
