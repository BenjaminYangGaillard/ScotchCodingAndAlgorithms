import sys
import threading
from collections import deque

def main():
    import sys
    input = sys.stdin.readline

    N, M, K, D = map(int, input().split())
    b = list(map(int, input().split()))

    # build adjacency list
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        adj[u].append(v)
        adj[v].append(u)

    def can_send(L):

        if b[0] < L:
            return False
        visited = [False]*N
        q = deque([0])
        visited[0] = True
        count = 1
        depth = 0

        while q and depth < D:
            for _ in range(len(q)):
                u = q.popleft()
                for v in adj[u]:
                    if not visited[v] and b[v] >= L:
                        visited[v] = True
                        q.append(v)
                        count += 1
                        if count >= K:
                            return True
            depth += 1

        return count >= K

    # binary search over answer L
    low, high = 1, max(b)
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if can_send(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print(ans)

if __name__ == "__main__":
    # increase recursion limit / stack size if needed
    threading.Thread(target=main).start()

