tc = int(input())

for t in range(1, tc + 1):
    arr = list(map(int, input().split()))
    arr.sort()  # 배열 정렬

    temp = arr[1:len(arr) - 1]
    answer = round(sum(temp) / len(temp))

    print("#%d %d" % (t, answer))
