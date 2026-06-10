#그래프 리스트

t = int(input())

for _ in range(t):
    N,M = map(int,input().split())

    Matrix = [[] for _ in range(N)]

    for i in range(M):
        u,v = map(int,input().split())
        Matrix[u].append(v)
        Matrix[v].append(u)

    for i in range(N):
        Matrix[i].sort()
        print(*Matrix[i]) #print(sorted(*Matrix[i]))
    