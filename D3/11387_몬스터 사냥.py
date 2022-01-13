tc = int(input())

for t in range(1, tc + 1):
    d, l, n = map(int, input().split())
    damage = 0
    for i in range(n):
        damage += d * (1 + i * l * 0.01)

    print("#%d %d" % (t, damage))
