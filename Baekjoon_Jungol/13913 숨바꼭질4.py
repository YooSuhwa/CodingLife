MAX = 200000
n, m = map(int, input().strip().split(' '))

visit = [False]*MAX
dist = [-1]*MAX
way = [-1]*MAX

q = []
q.append(n)
visit[n] = True
dist[n] = 0
while q:
    now = q.pop(0)

    for i in range(0, 3):
        if i == 0 :
            next = now+1
            if next>=MAX and visit[next]:
                continue
        elif i == 1 :
            next = now-1
            if next<0 and visit[next]:
                continue
        elif i == 2 :
            next = now*2
            if next>=MAX and visit[next]:
                continue

        q.append(next)
        visit[next] = True
        dist[next] = dist[now] + 1
        way[next] = now

print(dist[m])
