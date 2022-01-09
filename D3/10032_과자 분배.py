tc = int(input())

for t in range(1, tc + 1):
    n, k = map(int, input().split())

    # 과자의 개수가 사람의 수의 배수라면 모두 분배 가능
    if n % k == 0:
        print("#%d %d" % (t, 0))
    # 과자의 개수가 사람의 수의 배수가 아니라면 반드시 1개 차이가 난다.
    else:
        print("#%d %d" % (t, 1))
