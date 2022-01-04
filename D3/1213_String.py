for t in range(1, 11):
    test_case = int(input())
    temp = input()
    s = input()
    answer = s.count(temp)

    print("#%d %d" % (test_case, answer))
