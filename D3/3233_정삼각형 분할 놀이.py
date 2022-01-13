tc = int(input())

for t in range(1, tc + 1):
    a, b = map(int, input().split())
    # 삼각형의 넓이 공식을 활용
    answer = a ** 2 // b ** 2

    print("#%d %d" % (t, answer))
