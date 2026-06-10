def Sum(A):
    s = 0
    s = s + sum(A[:])
    return s

t = int(input())
for _ in range(t):
    A = list(map(int,input().split()))
    print(Sum(A))