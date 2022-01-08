tc = int(input())

for t in range(1, tc + 1):
    number = int(input())
    answer = 0

    if number % 2 == 0:
        # 짝수의 절반 - 1 까지 탐색
        # ex) 16이면 7까지 탐색
        for y in range(1, number // 2):
            temp = 0
            for x in range(y, number // 2):
                temp += x
                if temp == number:
                    answer += 1
                    break
                elif temp > number:
                    break
    else:
        # 홀수의 절반보다 1더 큰 수까지 탐색
        # ex) 15이면 8까지 탐색
        for y in range(1, number // 2 + 2):
            temp = 0
            for x in range(y, number // 2 + 2):
                temp += x
                if temp == number:
                    answer += 1
                    break
                elif temp > number:
                    break

    if number == 1:
        answer = 0
    print("#%d %d" % (t, answer + 1))
