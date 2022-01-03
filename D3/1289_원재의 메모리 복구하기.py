tc = int(input())

for t in range(1, tc + 1):
    answer = list(map(int, input().strip()))
    cnt = 0
    # 맨 앞이 1 이라면 횟수 1 증가 --> 초기화 상태의 bit가 모두 0이기 때문에
    if answer[0] == 1:
        cnt += 1

    # 값이 다른 것이 나올 때마다 횟수 증가
    for i in range(len(answer) - 1):
        if answer[i] != answer[i + 1]:
            cnt += 1
    print("#%d %d" % (t, cnt))
