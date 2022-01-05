tc = int(input())

for t in range(1, tc + 1):
    person = int(input())
    seat = list(map(int, input().split()))
    answer = 0
    # 앉을 수 있는 좌석 수를 오름차순 정렬
    seat.sort()
    # 우선 사람 수 (앉아 있는 좌석 수) + 양 끝 좌석을 미리 더해준다.
    answer += (person + seat[0] + seat[-1])
    for i in range(person - 1):
        answer += seat[i + 1]

    print("#%d %d" % (t, answer))
