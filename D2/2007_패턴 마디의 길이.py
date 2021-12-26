tc = int(input())

for t in range(1, tc + 1):
    arr = list(input().strip())
    # 전략: 첫 글자와 같은 인덱스마다 그 길이만큼의 다음구간을 검사
    # 같다면 break 틀리면 continue
    start = arr[0]
    length = 0
    index = 0
    # korea korea
    for i in range(1, len(arr)):
        # 첫 글자와 같은 문자가 등장했을 때
        if start == arr[i]:
            length = i
            # 0번부터 i-1 번까지의 문자열과 그 길이만큼의 다음 구간의 문자열을 비교
            if arr[0:i] == arr[i:i + length]:
                print("#%d %d" % (t, length))
                break
