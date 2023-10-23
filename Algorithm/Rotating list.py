A = [int(x) for x in input().split()]


def findMaxIdx(A, idx):
    '''A 리스트에서 최댓값의 인덱스를 찾는 함수'''
    global max_idx
    if len(A) == 1:   # 비교횟수: 1번
        max_idx = idx
        return
    elif len(A) == 2:  # 비교횟수: 1번
        if A[0] > A[1]:  # 비교횟수: 1번
            max_idx = idx
        else:
            max_idx = idx + 1
        return
    mid = len(A) // 2
    if A[mid] > A[0]:               # 비교횟수: 1번
        findMaxIdx(A[mid:], idx + mid)  # 비교횟수: T(n/2)
    else:
        findMaxIdx(A[:mid], idx)      # 비교횟수: T(n/2)


max_idx = 0
findMaxIdx(A, 0)
print(len(A) - max_idx - 1)
'''
findMaxIdx 함수(전체 알고리즘)의 비교횟수
T(n) = T(n/2) + 4 = O(logn)
'''
