tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    arr = []
    for _ in range(n):
        s = input()
        arr.append(s[0].upper())

    arr = list(set(arr))
    arr.sort()
    print(arr)
    ch = 65
    answer = 0
    for i in range(len(arr)):
        if ord(arr[i]) == ch:
            answer += 1
            ch += 1
        else:
            break

    print("#%d %d" % (t, answer))
