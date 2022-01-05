tc = int(input())

for t in range(1, tc + 1):
    number = list(input())
    answer = [number[0]]

    for i in range(len(number) - 1):
        if number[i + 1] in answer:
            answer.remove(number[i + 1])
        else:
            answer.append(number[i + 1])

    print("#%d %d" % (t, len(answer)))
