n = int(input())

for i in range(1, n + 1):
    cnt = 0
    temp = i
    while temp != 0:
        # 매 숫자마다 3,6,9가 몇 개 들어있는 지 검사
        if temp % 10 == 3 or temp % 10 == 6 or temp % 10 == 9:
            cnt += 1
        temp //= 10
    # 박수를 치지 않는다면 그냥 숫자를 출력
    if cnt == 0:
        print(i, end=" ")
    # 박수를 쳐야 한다면, cnt만큼 박수를 출력
    else:
        s = ""
        for clap in range(cnt):
            s += "-"
        print(s, end=" ")
