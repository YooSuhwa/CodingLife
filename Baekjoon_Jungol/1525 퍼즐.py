'''
   @ ush 2019/12/30
   * 백준 알고리즘 - 1525 퍼즐 (https://www.acmicpc.net/problem/1525)
   * python

   * BFS

   * 8퍼즐을 푸는 문제
   * 상태의 수가 많기때문에 배열로 저장할 수가 없다. 
        따라서 dict()를 이용 (c++ map / java hashMap 이용하여 저장)
   * 1. 빈칸을 숫자 9로 두고, 빈칸(9)의 위치를 구한 후 상하좌우로 하나씩 bfs
   * 2. 상하좌우로 바꾸는 next가 dist에 없으면 q.push(next)
   * 3. 최종적으로 dist[123456789]가 존재하면 출력. 아니면 -1을 출력한다. 
'''
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

            if dist.get(next, -1) == -1: #next not in dist
                q.append(next)
                dist[next] = dist[now]+1

print(dist.get(123456789, -1))
