tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    cnt = [0] * 10
    temp = 0
    multi = 1
    answer = 0
    # cnt의 0의 개수가 0이 될때까지 while반복
    while cnt.count(0) != 0:
        temp += (n * multi)
        answer = temp
        while temp != 0:
            cnt[temp % 10] += 1
            temp //= 10
        multi += 1

    print("#%d %d" % (t, answer))
