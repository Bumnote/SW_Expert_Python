tc = int(input())

for t in range(1, tc + 1):
    p, q = map(float, input().split())
    # 올바르지 않은 면 --> 뒤집고 --> 정상적으로 꽂힐 때
    s1 = (1 - p) * q
    # 올바른 면인데 제대로 꽂히지 않아서 --> 다시 뒤집고 --> 다시 꼽기
    s2 = p * (1 - q) * q

    if s1 < s2:
        print("#%d %s" % (t, "YES"))
    else:
        print("#%d %s" % (t, "NO"))
