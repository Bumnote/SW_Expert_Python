tc = int(input())

for t in range(1, tc + 1):
    # 7개의 정수를 입력받는다.
    number = list(map(int, input().split()))
    arr = []
    Sum = 0
    for i in range(len(number) - 2):
        for j in range(i + 1, len(number) - 1):
            for w in range(j + 1, len(number)):
                # 3개의 수를 더한 값들을 계속 append 시킨다.
                Sum += (number[i] + number[j] + number[w])
                arr.append(Sum)
                Sum = 0
    # 중복되는 값을 없애기 위해서 set 함수를 활용한다.
    answer = list(set(arr))
    answer.sort()

    print("#%d %d" % (t, answer[-5]))
