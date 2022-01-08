tc = int(input())

for t in range(1, tc + 1):
    s = input()
    answer = []
    for i in range(len(s)):
        if s[i] not in answer:
            answer.append(s[i])
        else:
            answer.remove(s[i])

    answer.sort()
    print("#%d" % t, end=" ")
    if len(answer) == 0:
        print("Good")
    else:
        for i in answer:
            print(i, end="")
        print()
