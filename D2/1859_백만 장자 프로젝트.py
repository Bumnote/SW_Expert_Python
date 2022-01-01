tc = int(input())

for t in range(1, tc + 1):
    # 기본 요소
    n = int(input())
    arr = list(map(int, input().split()))
    # 문제 풀이 변수들 초기화
    answer = 0  # 정답
    max_index = 0  # 범위 내의 가장 큰 값의 위치값
    max_value = arr[max_index]
    start_index = 0  # 범위 탐색의 시작점

    # 전체 탐색 - 범위 내의 가장 큰 값에서 다 팔아야 한다.
    while True:
        # 범위 내에서 최대 가격과 그 위치를 찾는다.
        for i in range(start_index, len(arr)):
            if max_value <= arr[i]:
                max_value = arr[i]
                max_index = i

        # 최댓값과의 차이값(=순이익)을 모두 더해준다.
        for i in range(start_index, max_index + 1):
            answer += (arr[max_index] - arr[i])

        start_index = max_index + 1
        # 시작 위치값이 배열 길이와 같아지면 알고리즘 종료
        if start_index == len(arr):
            break
        max_value = -1  # 최대 가격 초기화

    print("#%d %d" % (t, answer))
