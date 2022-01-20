def solution(number):

    multiplesSum = 0

    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            multiplesSum += i

    return multiplesSum
    

print(solution(10))
print(solution(20))