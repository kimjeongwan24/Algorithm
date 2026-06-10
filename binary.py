#이진탐색 재귀함수

def binary(data,left,right,q):
    if left>right:
        return -1
    
    mid = (left+right) // 2

    if data[mid] == q:
        return mid
    
    if data[mid] < q:
        solve = binary(data,mid+1,right,q)
    elif data[mid] > q:
        solve = binary(data,left,mid-1,q)
    return solve




t = int(input())
for _ in range(t):
    data = list(map(int,input().split()))
    query = list(map(int,input().split()))
    answer = []

    for q in query:
        answer.append(binary(data,0,len(data)-1,q))

    print(*answer)