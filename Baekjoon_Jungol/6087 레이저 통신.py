'''
   @ 2020.01.04 ush
   * 백준 알고리즘 - 6087 레이저 통신 (https://www.acmicpc.net/problem/6087)
   * python
   * BFS

   * 두 C를 레이저로 연결하기 위해서 설치해야 하는 최소 거울의 개수를 구하는 문제
   * 거울의 개수를 구하는 것은 결국 필요한 '직선의 최소개수 -1'과 같다.
   * 1. 시작점, 도착점 C 찾기
   * 2. now 점에 대해서 상하좌우 직선 방향으로 가면서 dist++
   * 3. 도착점 C점에서의 dist는 필요한 최소의 직선 개수며, 최소의 거울 개수는 직선개수-1 이다.
'''
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

startX = startY = endX = endY = -1

w, h = map(int, input().split())
board = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            if startX == -1:
                startX = i
                startY = j
            else:
                endX = i
                endY = j

q = deque()
dist = [[-1]*w for i in range(h)]

q.append((startX, startY))
dist[startX][startY] = 0

while q:
    now = q.popleft()
    x = now[0]
    y = now[1]

    for k in range(4):
        newX = x + dx[k]
        newY = y + dy[k]

        while -1 < newX < h and -1 < newY < w:
            if board[newX][newY] == '*':
                break
            if dist[newX][newY] == -1:
                q.append((newX, newY))
                dist[newX][newY] = dist[x][y] + 1

            newX += dx[k]
            newY += dy[k]

print(dist[endX][endY] - 1)
