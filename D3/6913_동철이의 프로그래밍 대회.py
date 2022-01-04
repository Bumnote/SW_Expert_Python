tc = int(input())

for t in range(1, tc + 1):
    y, x = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(y)]
    problem_cnt = [0 for _ in range(y)]
    person_cnt = 0
    for i in range(y):
        for j in range(x):
            problem_cnt[i] += arr[i][j]

    person_cnt += problem_cnt.count(max(problem_cnt))
    print("#%d %d %d" % (t, person_cnt, max(problem_cnt)))
