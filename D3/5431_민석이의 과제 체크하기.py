tc = int(input())

for t in range(1, tc + 1):
    person, perfect = map(int, input().split())
    temp = set([i for i in range(1, person + 1)])
    wrong = set(list(map(int, input().split())))
    answer = list(temp - wrong)

    print("#%d" % t, end=" ")
    for i in answer:
        print(i, end=" ")
    print()
