from collections import deque

def bfs(num):
    q = deque()
    dist = [-1] * num
    way = [-1 ] * num
    how = [-1] * num

    temp = 1%num
    q.append(temp)
    dist[temp] = 0

    how[temp] = 1

    while q :
        now = q.popleft()
        for i in [0,1]:
            next = (now*10 + i)
            next %= num
            if dist[next] == -1:
                dist[next] = dist[now] +1
                way[next] = now #from
                how[next] = i
                q.append(next)

    if dist[0] == -1 :
        print("BRAK")
        return

    answer = ""
    i = 0
    while i!= -1:
        answer += str(how[i])
        i = way[i]

    print(answer[::-1])

testCase = int(input())
for _ in range(testCase):
    num = int(input())
    bfs(num)