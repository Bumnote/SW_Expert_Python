tc = int(input())

for t in range(1, tc + 1):
    n, m = map(int, input().split())
    b_number = int(bin(m)[2:])

    temp = 0
    answer = (2 ** n) - 1
    # for 반복문의 index 를 활용하여 2진수를 구현한다.
    for i in range(n):
        temp += (b_number % 10) * (2 ** i)
        b_number //= 10
        if b_number == 0:
            break

    if answer == temp:
        print("#%d %s" % (t, "ON"))
    else:
        print("#%d %s" % (t, "OFF"))
