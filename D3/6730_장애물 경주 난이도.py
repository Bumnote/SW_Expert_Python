tc = int(input())

for t in range(1, tc + 1):
    cnt = int(input())
    height = list(map(int, input().split()))
    up = 0
    down = 0
    for i in range(len(height) - 1):
        if height[i] <= height[i + 1]:
            if up < height[i + 1] - height[i]:
                up = height[i + 1] - height[i]
        else:
            if height[i] > height[i + 1]:
                if down < height[i] - height[i + 1]:
                    down = height[i] - height[i + 1]

    print("#%d %d %d" % (t, up, down))
