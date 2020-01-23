from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(s, e):
    count = 1
    q = deque()

    q.append((s,e))
    visit[s][e] = True

    while q :
        (x,y) = q.popleft()

        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]

            if not (-1 < newX < n):
                continue
            if not (-1 < newY < n):
                continue

            if board[newX][newY] == '0':
                continue

            if not visit[newX][newY] :
                q.append((newX,newY))
                visit[newX][newY] = True
                count +=1
    return count

n = int(input())

board = []
for _ in range(n):
    board.append(input())

visit = [[False] * n for _ in range(n)]
answer = []

for i in range(n):
    for j in range(n):
        if board[i][j] =='1' and (not visit[i][j]):
            answer.append(bfs(i,j))

answer.sort()

print(len(answer))
print('\n'.join(map(str, answer)))

