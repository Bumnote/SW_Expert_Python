tc = int(input())

for t in range(1, tc + 1):
    # 5개의 단어 --> 5줄
    Words = [[" "] * 15 for _ in range(5)]
    for y in range(5):
        s = input()
        for x in range(len(s)):
            Words[y][x] = s[x]

    answer = ""
    for x in range(15):
        for y in range(5):
            if Words[y][x] != " ":
                answer += Words[y][x]
            else:
                continue

    print("#%d %s" % (t, answer))
