tc = int(input())

for t in range(1, tc + 1):
    n, k = map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    arr = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        arr.append(a * 0.35 + b * 0.45 + c * 0.2)

    student = arr[k - 1]
    arr.sort(reverse=True)
    # n명의 학생들을 정확한 비율로 성적을 준다.
    print("#%d %s" % (t, grade[arr.index(student) // (n // 10)]))
