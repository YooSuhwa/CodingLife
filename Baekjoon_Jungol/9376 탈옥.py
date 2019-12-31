from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def makeBFS (board, x, y, h, w):
    q = deque()
    dist = [[-1]*w for _ in range(h)]

    q.append((x,y))
    dist[x][y] = 0

    while q :
        now = q.popleft()
        x = now[0]
        y = now[1]

        for k in range(0, 4):
            newX = x + dx[k]
            newY = y + dy[k]

            if (-1< newX < h) and (-1 < newY < w):

                if dist[newX][newY] != -1:
                    continue
                if board[newX][newY] == '*' :# 벽
                    continue
                if board[newX][newY] == '#' : #문
                    dist[newX][newY] = dist[x][y] + 1
                    q.append((newX, newY))
                else : #빈공간
                    dist[newX][newY] = dist[x][y]
                    q.appendleft((newX, newY))
    return dist

t = int(input())
for _ in range(t):
    h, w = map(int, input().strip().split(' '))

    board = []
    for i in range(0, h):
        board.append('.' + input() + '.')
    h += 2
    w += 2
    board = ['.' * w] + board + ['.' * w]
    # bfs0 : from external point (0,0) / bfs1 : prisoner1 / bfs2 : prisoner2
    bfs0 = makeBFS(board, 0, 0, h, w)