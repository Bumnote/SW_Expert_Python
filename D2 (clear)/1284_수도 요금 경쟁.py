tc = int(input())

for t in range(1, tc + 1):
    p, q, r, s, w = map(int, input().split())
    A = p * w
    B = q + (w - r) * s if w >= r else q

    if A < B:
        print("#%d %d" % (t, A))
    else:
        print("#%d %d" % (t, B))
