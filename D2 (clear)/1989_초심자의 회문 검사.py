tc = int(input())

for t in range(1, tc + 1):
    # 배열로 받아서 뒤집었을 때와 결과가 같으면 palindrome
    s = list(input().strip())
    temp = s.copy()  # deep copy
    s.reverse()

    if s == temp:
        print("#%d %d" % (t, 1))

    else:
        print("#%d %d" % (t, 0))
