import sys
from bisect import bisect_left

input = sys.stdin.readline

def find_closest(arr, target):
    idx = bisect_left(arr, target)
    
    candidates = []
    if idx < len(arr):
        candidates.append(arr[idx])
    if idx > 0:
        candidates.append(arr[idx - 1])
    
    # 차이가 같으면 작은 값 반환
    return min(candidates, key=lambda x: (abs(x - target), x))

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    
    result = [find_closest(arr, q) for q in queries]
    print(*result)