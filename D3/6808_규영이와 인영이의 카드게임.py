from itertools import permutations # 순열 라이브러리

tc = int(input())

for t in range(1, tc + 1):
    # 카드의 숫자는 1 ~ 18
    A = list(map(int, input().split()))
    # 1 ~ 18 까지의 숫자 중에서 A에 없으면 B의 원소로 가지게 하는 list comprehension
    B = [i for i in range(1, 19) if i not in A]
    # map 함수를 이용해서 tuple 형을 list 형으로 변환
    permutation = list(map(list, permutations(B, 9)))

    Sum_A = 0
    Sum_B = 0

    Gyu_Win = 0
    Gyu_Lose = 0
    for i in range(len(permutation)):
        Sum_A = 0
        Sum_B = 0
        for j in range(9):
            if A[j] > permutation[i][j]:
                Sum_A += (A[j] + permutation[i][j])
            else:
                Sum_B += (A[j] + permutation[i][j])
        if Sum_A > Sum_B:
            Gyu_Win += 1
        elif Sum_A < Sum_B:
            Gyu_Lose += 1

    print("#%d %d %d" % (t, Gyu_Win, Gyu_Lose))
