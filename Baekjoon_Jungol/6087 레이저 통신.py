from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

startX = startY = endX = endY = -1

w,h = map(int,input().split())
board = [input() for _ in range(n)]
#board =['.......','......C','......*','*****.*','....*..','....*..','.C..*..','.......']


for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            if startX ==-1 :
                startX = i
                startY = j
            else :
                endX = i
                endY = j


q = deque()
dist = [-1 * h] for _ in range(w)

q.append((startX, startY))
dist[startX][startY] = 0

while q :
    now = q.popleft()
    x = now[0]
    y = now[1]
    
    for k in range(4):
        newX = x + dx[k]
        newY = y + dy[k]
        
        while -1<newX<h and -1<newY<w:
            if board[newX][newY] == '*' :
                break
            if dist[newX][newY] == -1:
                q.append((newX, newY))
                dist[newX][newY] = dist[x][y]+1
            
            newX += dx[k]
            newY += dy[k]

print(dist[endX][endY]-1)