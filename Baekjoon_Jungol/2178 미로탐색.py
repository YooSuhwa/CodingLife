from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, m = map(int, input().strip().split(' '))
board = []
for _ in range(n):
    board.append(input())

q = deque()
dist = [[0] * m for _ in range(n)]

q.append((0,0))
dist[0][0] = 1

while q:
    (x, y) = q.popleft()

    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]

        if not (-1<newX<n) :
            continue
        if not (-1<newY<m) :
            continue

        if board[newX][newY] == '0':
            continue

        if dist[newX][newY] == 0 :
            dist[newX][newY] = dist[x][y] + 1
            q.append((newX, newY))

print(dist[n-1][m-1])