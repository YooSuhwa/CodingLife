
from collections import deque
puzzleSize = 3
dx = [0,0,1,-1]
dy = [1,-1,0,0]
puzzle = [list(map(int,input().split())) for _ in range(puzzleSize)]
start = 0
for i in range(puzzleSize):
    for j in range(puzzleSize):
        temp = puzzle[i][j]
        if temp == 0:
            temp = 9
        start = start*10 + temp

q = deque()
dist = dict()

q.append(start)
dist[start] = 0

while q :
    now = q.popleft()
    nowStr = str(now)

    #빈칸위치 찾기
    emptyPos = nowStr.find('9')
    emptyX = emptyPos//puzzleSize
    emptyY = emptyPos%puzzleSize

    for i in range(4):
        newX = emptyX+dx[i]
        newY = emptyY+dy[i]

        if -1 < newX < puzzleSize and -1 < newY < puzzleSize :
            temp = list(nowStr)
            temp[emptyX*3+emptyY],temp[newX*3+newY] = temp[newX*3+newY],temp[emptyX*3+emptyY]
            next = int(''.join(temp))

            if dist.get(next, -1) == -1:
                q.append(next)
                dist[next] = dist[now]+1

print(dist.get(123456789, -1))
