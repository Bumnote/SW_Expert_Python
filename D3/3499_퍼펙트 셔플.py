tc = int(input())

for t in range(1, tc + 1):
    cnt = int(input())
    Card = list(input().split())
    first = []
    second = []
    answer = []
    # 카드가 짝수 개면 개수가 딱 맞는다.
    if cnt % 2 == 0:
        first = Card[:cnt // 2]
        second = Card[cnt // 2:]
        for i in range(cnt // 2):
            answer.append(first[i])
            answer.append(second[i])
    # 카드가 홀수이면, 홀수 개 만큼 반복하고 첫 덱에 있는 마지막 카드를 더해준다.
    else:
        first = Card[:cnt // 2 + 1]
        second = Card[cnt // 2 + 1:]
        for i in range(cnt // 2):
            answer.append(first[i])
            answer.append(second[i])
        answer += [first[-1]]

    print("#%d" % t, end=" ")
    for i in answer:
        print(i, end=" ")
    print()
