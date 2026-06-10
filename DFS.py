#DFS 재귀함수

import sys
sys.setrecursionlimit(1000000)

def DFS(v,list,check):
    print(v, end = " ")
    check[v] = True
    for next in list[v]:
        if check[next] == False:
            DFS(next,list,check)


t = int(input())

for _ in range(t):
    N,M = map(int,input().split())
    list = [[] for _ in range(N)]

    for i in range(M):
        u, v = map(int,input().split())
        list[u].append(v)
        list[v].append(u)

    for i in range(N):
        list[i].sort()

    check = [False]*N
    DFS(0,list,check)
    print("")