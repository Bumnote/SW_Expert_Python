tc = int(input())

for t in range(1, tc + 1):
    test_case = int(input())
    grade = list(map(int, input().split()))
    cnt = -1
    answer = -1

    for i in grade:
        # 최빈수면 answer = i
        if cnt < grade.count(i):
            cnt = grade.count(i)
            answer = i
        # 최빈수가 여러개인 경우 더 큰 값을 가진 값이 정답
        elif cnt == grade.count(i):
            if answer < i:
                answer = i
        # 최빈수보다 적은 경우는 다시 조건으로 돌아간다.
        else:
            continue

    print("#%d %d" % (test_case, answer))
