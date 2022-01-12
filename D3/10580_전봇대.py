tc = int(input())

for t in range(1, tc + 1):
    n = int(input())  # 전선의 개수
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
        # ai , bi --> 전선이 부착된 높낮이

    answer = 0
    for i in range(n - 1):
        x = arr[i][0]
        y = arr[i][1]
        for j in range(i + 1, n):
            #  [ 1  5 ] [ 2  4 ] 와 같은 경우
            if x < arr[j][0] and y > arr[j][1]:
                answer += 1
            #  [ 2  4 ] [ 1  5 ] 와 같은 경우
            if x > arr[j][0] and y < arr[j][1]:
                answer += 1

    print("#%d %d" % (t, answer))
