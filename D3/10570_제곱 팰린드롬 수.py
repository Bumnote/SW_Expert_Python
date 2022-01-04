from math import sqrt  # math 모듈에서 sqrt만 사용

def isTrue(n):
    arr = str(n)
    arr_reverse = arr[::-1]
    temp = ""
    # 제곱근이 정수라면 계속 진행
    if int(sqrt(n)) == sqrt(n):
        temp = str(int(sqrt(n)))
    # 제곱근이 정수가 아니라면 return
    else:
        return 0
    temp_reverse = temp[::-1]
    if arr == arr_reverse and temp == temp_reverse:
        return 1
    else:
        return 0


tc = int(input())

for t in range(1, tc + 1):
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b + 1):
        if isTrue(i):
            cnt += 1

    print("#%d %d" % (t, cnt))
