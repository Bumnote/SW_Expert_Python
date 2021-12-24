tc = int(input())

for t in range(1, tc + 1):
    a, b = map(int, input().split())
    res = a // b
    mod = a % b
    
    print("#%d %d %d" % (t, res, mod))
