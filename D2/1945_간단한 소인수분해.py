tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    cnt = [0] * 5
    arr = [2, 3, 5, 7, 11]
    index = 0
    while True:
        while n % arr[index] == 0:
            cnt[index] += 1
            n //= arr[index]
        index += 1
        if index == len(arr):
            break

    print("#%d" % t, end=" ")
    for i in cnt:
        print(i, end=" ")
    print()