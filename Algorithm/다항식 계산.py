import time
import random


def evaluate_n2(A, x):
    # code for O(n^2)-time function
    res = 0
    for k in range(n):
        term = A[k]
        for _ in range(k):
            term *= x
        res += term
    return res


def evaluate_n(A, x):
    # code for O(n)-time function
    res = 0
    var = 1
    for k in range(n):
        res += A[k] * var
        var *= x
    return res


random.seed()		# random 함수 초기화
# n 입력받음
n = int(input())
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A = []
for _ in range(n):
    A.append(random.randint(-1000, 1000))
# x값 생성
x = random.randint(-1000, 1000)
# evaluate_n2 호출
s = time.process_time()
evaluate_n2(A, x)
e = time.process_time()
# evaluate_n 호출
s2 = time.process_time()
evaluate_n(A, x)
e2 = time.process_time()
# 두 함수의 수행시간 출력
print("evaluate_n2 수행시간 =", e-s)
print("evaluate_n 수행시간 =", e2-s2)
