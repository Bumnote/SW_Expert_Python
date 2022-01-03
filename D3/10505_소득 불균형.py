tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    person = list(map(int, input().split()))
    cnt = 0
    avg = sum(person) / len(person)
    
    for i in range(len(person)):
        if person[i] <= avg:
            cnt += 1

    print("#%d %d" % (t, cnt))
