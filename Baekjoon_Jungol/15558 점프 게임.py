from collections import deque

n, k = map(int, input().strip().split(' '))
board = [input() for _ in range(2)]
dxy = [(0,1), (0,-1), (1,k)]

q = deque()
dist = [[-1]*n for i in range(2)]

q.append((0,0))
dist[0][0] = 0

flag = False

while q:
    (x,y) = q.popleft()
    for (dx, dy) in dxy:
        newX = (x + dx)%2
        newY = y + dy

        if newY >= n :
            flag = True
            break
        if newY <0 :
            continue

        if board[newX][newY]== '0':#이동할 수 없는 칸
            continue

        if newY < dist[newX][newY]+1 :#해당 newY칸을 방문 했을 때의 dist가 같거나 커야 방문할 수 있다.
            continue

        if dist[newX][newY] == -1 :
            dist[newX][newY] = dist[x][y] + 1
            q.append((newX, newY))

    if flag :
        break

if flag== True:
    print(1)
else:
    print(0)