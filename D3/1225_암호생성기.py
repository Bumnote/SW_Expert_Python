from collections import deque

for t in range(1, 11):
    test_case = int(input())
    answer = deque(list(map(int, input().split())))
    minus = 1

    while True:
        answer.append(answer[0] - minus)
        answer.popleft()
        if answer[-1] <= 0:
            answer[-1] = 0
            break
        minus += 1
        if minus == 6:
            minus = 1

    print("#%d" % t, end=" ")
    for i in answer:
        print(i, end=" ")
    print()
