tc = int(input())

for t in range(1, tc + 1):
    horn, animal = map(int, input().split())
    unicorn = 0
    twinhorn = 0

    for i in range(animal + 1):
        unicorn = 1 * i
        twinhorn = 2 * (animal - i)
        if horn == unicorn + twinhorn:
            unicorn = i
            twinhorn = animal - i
            break

    print("#%d %d %d" % (t, unicorn, twinhorn))
