from collections import deque
MAX = 200001

start, find = map(int, input().strip().split(' '))

q = deque()
visit = [False]*MAX
dist = [-1]*MAX
count = [0]*MAX

q.append(start)
visit[start] = True
dist[start] = 0
count[start] = 1

while q :
    now = q.popleft()
    nextList  = [now-1, now+1, now*2]

    for next in nextList:
        if -1 < next < MAX:
            if not visit[next]:
                q.append(next)
                visit[next] = True
                dist[next] = dist[now] + 1
                count[next] = count[now]

                if dist[next] == dist[now] + 1:
                    count[next] += count[now]

print(dist[find])
print(count[find])
