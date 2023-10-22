def max_sum(A, left, right):
    # A[left], ..., A[right] 중 최대 구간 합 리턴
    # 아래 3줄의 수행시간: c(상수)
    if left == right:
        return A[left]
    m = (left + right) // 2

    # 아래 2줄의 수행시간: 2T(n/2)
    L = max_sum(A, left, m)      # 수행시간: T(n/2)
    R = max_sum(A, m + 1, right)  # 수행시간: T(n/2)

    # 아래 14줄의 수행시간: O(n)
    max_left_ps = A[m]
    cur_left_ps = A[m]
    for i in range(m-1, left-1, -1):
        cur_left_ps += A[i]
        if cur_left_ps > max_left_ps:
            max_left_ps = cur_left_ps
    max_right_ps = A[m+1]
    cur_right_ps = A[m+1]
    for i in range(m+2, right+1):
        cur_right_ps += A[i]
        if cur_right_ps > max_right_ps:
            max_right_ps = cur_right_ps
    M = max_left_ps + max_right_ps
    return max(L, M, R)


A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)
'''
알고리즘 설명: A를 반으로 분할하면 최대 구간 합이 존재하는 경우는 딱 3가지다. 
1. A의 왼쪽 반 구간에 존재
2. A의 오른쪽 반 구간에 존재
3. A의 양쪽에 모두 걸치는 경우
A의 왼쪽 반 구간에서의 최대 구간 합을 L, A의 양쪽에 모두 걸치는 최대 구간 합을 M, A의 오른쪽 반 구간에서의 최대 구간 합을 R이라고 하자. 그러면 L, M, R 중에서 최댓값이 최종적인 최대 구간 합이 된다. L과 R은 같은 방식을 사용하여 재귀로 구하고, M은 L의 가장 끝 수부터 왼쪽으로 prefix-sum을 구하면서 가장 큰 구간을 찾고, R의 첫 수부터 오른쪽으로 prefix-sum을 구하면서 가장 큰 구간을 찾아 두 구간의 합을 더하면 구할 수 있다.
'''
'''
수행시간 분석
T(n) = 2T(n/2) + cn = O(nlogn)
'''
