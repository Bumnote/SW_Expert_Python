for t in range(1, 11):
    length = int(input())
    ch = [list(input().strip()) for _ in range(8)]
    answer = 0

    # 가로 검사
    for y in range(8):
        for x in range(8 - length + 1):
            # 회문 검사 길이만큼 검사
            s = ch[y][x:x + length]
            e = s.copy()
            e.reverse()
            if s == e:
                answer += 1
    # 세로 검사
    for y in range(8 - length + 1):
        for x in range(8):
            s= []
            # 세로는 리스트 슬라이싱이 안되기 때문에 3중 for문 사용
            for w in range(length):
                s.append(ch[y+w][x])
            e = s.copy()
            e.reverse()
            if s == e:
                answer += 1

    print("#%d %d" % (t, answer))
