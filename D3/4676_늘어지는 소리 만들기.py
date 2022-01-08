tc = int(input())

for t in range(1, tc + 1):
    Word = list(input())
    n = int(input())
    arr = list(map(int, input().split()))

    # 하이픈의 최대 개수는 100개
    count = [""] * (len(Word) + 1)
    for i in range(len(arr)):
        count[arr[i]] += "-"

    answer = ""
    for i in range(len(Word)):
        answer += count[i]
        answer += Word[i]
    answer += count[-1]
    print("#%d %s" % (t, answer))
