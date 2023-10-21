from sys import stdin as ss
from heapq import heappush, heappop
'''
자료구조와 알고리즘 설명

min_heap 1개와 max_heap 1개를 사용하였다.
A[0],...A[i]를 다음 조건을 만족하도록 두 힙에 분리해서 넣었다.
1. max_heap의 모든 값은 min_heap의 모든 값보다 작다.
2. max-heap의 개수를 k개로 유지하여 max_heap의 루트노드가 k번째 작은값이 되도록 한다.
'''

'''
수행시간: O(nlogn)
heappush와 heappop 모두 O(logn)의 시간 복잡도를 가지는데, for문에 의해 이를 n번 반복하기 때문이다.
'''

A = list(map(int, ss.readline().split()))  # n개의 서로 다른 정수 값을 리스트 A에 저장


def calcSum(A):
    '''
    m[i]값의 합을 반환
    '''
    mSum = 0  # m[i]값의 합
    # max_heap(파이썬의 heapq모듈에서는 min_heap을 제공하기 때문에 원소값에 -를 붙여서 heappush하면 max_heap을 만들 수 있다.)
    B = []
    S = []   # min_heap

    for i in range(len(A)):
        k = i//3 + 1
        # max_heap이 비어있거나, max_heap의 루트값보다 A[i]값이 작다면, -A[i] 삽입
        if not B or A[i] < -B[0]:
            heappush(B, -A[i])
        # 그 외의 경우, min_heap에 A[i] 삽입
        else:
            heappush(S, A[i])

        # max_heap의 루트노드 값을 k번째 작은 수로 만들기 위하여 max_heap의 크기를 k개로 유지
        if len(B) > k:
            heappush(S, -heappop(B))
        elif len(B) < k and S:
            heappush(B, -heappop(S))

        mSum -= B[0]

    return mSum


print(calcSum(A))
