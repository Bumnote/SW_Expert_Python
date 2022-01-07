for t in range(1, 11):
    length = int(input())

    answer = 0
    view = list(map(int, input().split()))
    for i in range(2, length - 2):
        # 해당 건물의 높이가 더 크다면
        if view[i - 2] < view[i] and view[i - 1] < view[i] and view[i + 1] < view[i] and view[i + 2] < view[i]:
            arr = [view[i - 2], view[i - 1], view[i + 1], view[i + 2]]
            # 해당 건물의 높이에서 양 옆 -2 ~ +2 범위 중 가장 큰 건물의 높이를 빼준 높이만큼이 조망권이 된다.
            answer += view[i] - max(arr)
        # 해당 건물의 크기가 작다면 다시 반복문으로 돌아간다.
        else:
            continue

    print("#%d %d" % (t, answer))
