tc = int(input())
everyday = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for t in range(1, tc + 1):
    test_case, number = input().split()
    count = [0] * 10

    day = list(input().split())
    for i in range(int(number)):
        count[everyday.index(day[i])] += 1

    print(test_case)
    for i in range(10):
        for j in range(count[i]):
            print(everyday[i], end=" ")
    print()
