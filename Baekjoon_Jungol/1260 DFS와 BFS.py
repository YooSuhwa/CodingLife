from collections import deque
def findV (vertex, visit, q, v, menu):
    find = []
    for (v1, v2) in vertex:
        if v1 == v and visit[v2]==False :
            find.append(v2)
        if v2 == v and visit[v1]==False :
            find.append(v1)

    if menu == 1 :
        find.sort(reverse=True)
    else :
        find.sort()

    return find


def dfs(vertex, s):
    answer = [s]
    q = deque()
    visit = [False] * (n+1)

    q.append(s)
    visit[s] = True

    while(q):
        v = q.pop()
        q.extend(findV(vertex, visit, q, v, 1))

        if not visit[v]:
            answer.append(v)
            visit[v] = True

    return ' '.join(map(str, answer))

def bfs(vertex, s):
    answer = [s]

    q = deque()
    visit = [False] * (n+1)

    q.append(s)
    visit[s] = True

    while(q):
        v = q.popleft()
        q.extend(findV(vertex, visit, q, v, 0))

        if not visit[v]:
            answer.append(v)
            visit[v] = True

    return ' '.join(map(str, answer))


n,m,start = map(int, input().strip().split(' '))
vertex = []

for _ in range(m):
    u,v = map(int, input().strip().split(' '))
    vertex.append((u,v))

print(dfs(vertex, start))
print(bfs(vertex, start))