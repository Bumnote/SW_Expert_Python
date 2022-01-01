arr = [["+"] * 5 for _ in range(5)]

for y in range(5):
    for x in range(5):
        if x == y:
            arr[y][x] = "#"
        print(arr[y][x], end="")
    print()
