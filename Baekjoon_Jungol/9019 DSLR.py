import sys
from collections import deque

MAX = 10001
sys.setrecursionlimit(MAX)
def go(n,m):
    if n == m :
        return
    go(n, way[m])
    print(how[m], end="")


test =  int(sys.stdin.readline())
for _ in range(0, test):
    a, b = map(int, input().strip().split(" "))

    q = deque()
    visit = [False]*MAX
    dist = [-1]*MAX
    way = [-1]*MAX
    how = ['']*MAX

    q.append(a)
    visit[a] = True
    dist[a] = 0
    way[a] = 0
    while q :
        now = q.popleft()

        next = int((now * 2) % 10000)
        if not visit[next] :
            how[next] = 'D'
            q.append(next)
            visit[next] = True
            dist[next] = dist[now] + 1
            way[next] = now

        next = now - 1
        if next == 0:
            next = 9999
        if not visit[next]:
            how[next] = 'S'
            q.append(next)
            visit[next] = True
            dist[next] = dist[now] + 1
            way[next] = now

        next = int((now%1000)*10 +(now/1000))
        if not visit[next]:
            how[next] = 'L'
            q.append(next)
            visit[next] = True
            dist[next] = dist[now] + 1
            way[next] = now

        nex = int((now %10)*1000 + (now/10))
        if not visit[next]:
            how[next] = 'R'
            q.append(next)
            visit[next] = True
            dist[next] = dist[now] + 1
            way[next] = now

    answer = ''
    while a != b:
        answer += how[b]
        b = way[b]
    print(''.join(reversed(answer)))