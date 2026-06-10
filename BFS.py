import sys
from collections import deque
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().split())
        
        adj = [[] for _ in range(N)]
        for _ in range(M):
            u, v = map(int, input().split())
            adj[u].append(v)
        
        # 낮은 번호 우선 → 인접 리스트 정렬
        for i in range(N):
            adj[i].sort()
        
        visited = [False] * N
        order = []
        
        queue = deque([0])
        visited[0] = True
        
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        print(*order)

solve()