tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    problem = list(map(int, input().split()))
    # 모두 틀린 경우인 0점을 초기값으로 넣어준다.
    # 중복 제거를 위해서 set 로 선언
    scores = {0}

    # 해당 list 내의 숫자들을 조합해서 나타낼 수 있는 모든 경우
    for p in problem:
        for s in list(scores):
            scores.add(s + p)

    print(f"#{t} {len(scores)}")
