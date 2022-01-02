def solution(a, b, answer):
    if b == 0:
        return answer
    answer *= a
    return solution(a, b - 1, answer)


for t in range(1, 11):
    tc = int(input())
    a, b = map(int, input().split())
    answer = solution(a, b, 1)

    print("#%d %d" % (t, answer))
