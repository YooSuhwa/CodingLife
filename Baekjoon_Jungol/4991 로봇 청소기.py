from collections import deque

def bfs (inx, iny):
    q = deque()
    dist = [[-1]*w for _ in range(h)]

    q.append((inx,iny))
    dist[inx][iny] = 0

    while q :
        (x, y) = q.popleft()

        for k in range(4):
            newX = x + dx[k]
            newY = y + dy[k]

            if (-1<newX<h) and (-1<newY <w):
                if dist[newX][newY] == -1 and board[newX][newY] != 'x': #가구 아니고 방문 아직 안함
                    dist[newX][newY] = dist[x][y] + 1
                    q.append((newX, newY))

    return dist

dx = [0,0,-1,1]
dy = [-1,1,0,0]
w, h = map(int, input().strip().split(' '))
board = [input() for _ in range(h)]

if w == 0 and h == 0 :
    exit()

q = deque()

for i in range(h):
    for j in range(w):
        temp = board[i][j]
        if temp == 'o' :
            q.appendleft((i, j))
        elif temp == '*' :
            q.append((i, j))

length = len(q)
dist = [[-1]*length for _ in range(length)]
flag = 0

for i in range(0, h):
    distEach = []
    distEach = bfs(q[i][0], q[i][1])
    for j in range (0, w):
        dist[i][j] = distEach[q[j][0]][q[j][0]]
        if dist[i][j] == -1 :
            flag = -1
            break

'''
if flag == -1 :
    print("-1")
    continue
    '''

answer = -1
while True :
    now = dist[0][1]

    for i in range(length-2):
        now += dist[i+1][i+2]

    if answer == -1 or answer > now :
        answer = now


print(answer)