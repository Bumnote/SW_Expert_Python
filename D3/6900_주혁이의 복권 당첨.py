tc = int(input())

for t in range(1, tc + 1):
    n, m = map(int, input().split())
    number = []
    price = []
    total_price = 0
    for _ in range(n):
        num, p = input().split()
        number.append(list(num))
        price.append(int(p))

    res = 0
    # 주혁이가 산 복권 수만큼 반복
    for i in range(m):
        arr = list(input())

        # 복권 당첨 번호에 비교하기
        for j in range(n):
            res = 0
            # 복권의 번호는 8자리 수이다.
            for w in range(8):
                # * 표시는 숫자로 대체할 수 있기 때문에 pass
                if number[j][w] == "*":
                    res += 1
                    continue
                else:
                    # * 이 아니면서 숫자와 일치하면 res += 1
                    if number[j][w] == arr[w]:
                        res += 1
            if res == 8:
                total_price += price[j]

    print("#%d %d" % (t, total_price))
