tc = int(input())

for t in range(1, tc + 1):
    cnt = int(input())
    arr = []
    index = 0
    for _ in range(cnt):
        ch, n = input().split()
        for _ in range(int(n.strip())):
            arr.append(ch.strip())

    print("#%d" % t)
    for i in arr:
        print(i, end="")
        index += 1
        if index == 10:
            index = 0
            print()
    print()