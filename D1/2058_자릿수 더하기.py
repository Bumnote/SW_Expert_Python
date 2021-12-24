n = int(input())
answer = 0
while n != 0:
    answer += (n % 10)
    n //= 10
print(answer)
