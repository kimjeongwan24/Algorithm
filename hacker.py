import sys
from collections import deque
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        
        adj = [[] for _ in range(N)]
        for _ in range(M):
            a, b = map(int, input().split())
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [False] * N
        count = 0
        
        for start in range(N):
            if not visited[start]:
                count += 1
                # BFS로 연결된 모든 컴퓨터 방문
                queue = deque([start])
                visited[start] = True
                while queue:
                    node = queue.popleft()
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
        
        print(count)

solve()