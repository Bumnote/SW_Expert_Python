tc = int(input())

for t in range(1, tc + 1):
    s1, s2 = input().split()
    flag = 0

    if len(s1) != len(s2):
        print("#%d %s" % (t, "DIFF"))
    else:
        for i in range(len(s1)):
            if s1[i] == 'A' or s1[i] == 'D' or s1[i] == 'O' or s1[i] == 'P' or s1[i] == 'Q' or s1[i] == 'R':
                if s2[i] == 'A' or s2[i] == 'D' or s2[i] == 'O' or s2[i] == 'P' or s2[i] == 'Q' or s2[i] == 'R':
                    flag += 1
                else:
                    continue
            elif s1[i] == 'B':
                if s2[i] == 'B':
                    flag += 1
                else:
                    continue
            else:
                if s2[i] == 'C' or s2[i] == 'E' or s2[i] == 'F' or s2[i] == 'G' or s2[i] == 'H' or s2[i] == 'I' or s2[
                    i] == 'J' or s2[i] == 'K' or s2[i] == 'L' or s2[i] == 'M' or s2[i] == 'N' or s2[i] == 'S' or s2[
                    i] == 'T' or s2[i] == 'U' or s2[i] == 'V' or s2[i] == 'W' or s2[i] == 'X' or s2[i] == 'Y' or s2[
                    i] == 'Z':
                    flag += 1
                else:
                    continue
        if flag == len(s1):
            print("#%d %s" % (t, "SAME"))
        else:
            print("#%d %s" % (t, "DIFF"))
