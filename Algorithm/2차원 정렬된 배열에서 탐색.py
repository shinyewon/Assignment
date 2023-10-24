n, K = tuple(map(int, input().split()))
matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]


def findKIdx(A, K, idx):
    '''1차원 배열 A에서 K값의 인덱스를 찾는 함수'''
    global j
    if len(A) == 0:
        return
    mid = len(A) // 2
    if K == A[mid]:
        j = idx + mid
        return
    elif K < A[mid]:
        findKIdx(A[:mid], K, idx)
    else:
        findKIdx(A[mid+1:], K, idx + mid + 1)


i, j = -1, -1
for row in range(n):
    findKIdx(matrix[row], K, 0)
    if j != -1:
        i = row
        break
print("(%d, %d)" % (i, j))

'''
<알고리즘 설명>
이차원 리스트 A에서 행별로 이진 탐색을 하여 K값이 있는지 찾았다.

<수행시간>
findKIdx 함수의 수행시간: T(n) = T(n/2) + c = O(logn)
전체 알고리즘의 수행시간: O(nlogn)
'''
