'''
   @ 2020/01/07 ush
   * 백준 알고리즘 - 15558 점프게임 (https://www.acmicpc.net/problem/15558)
   * python

   * BFS

   * 2개의 지도가 있을 때, 유저가 할 수 있는 행동은
    * 1. 한칸 위로 (0, 1)
    * 2. 한칸 뒤로 (0,-1)
    * 3. 옆칸으로 이동 후 k만큼 이동 (+1 mod 2, +k)
   * i초에 i번째 칸이 사라질 때, N번째 칸을 넘어갈 수 있는지 구하는 문제
'''
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

        if board[newX][newY] == '0':#이동할 수 없는 칸
            continue

        if newY <= dist[x][y] :#해당 newY칸을 방문 했을 때의 dist가 같거나 커야 방문할 수 있다.
            continue

        if dist[newX][newY] == -1 :
            dist[newX][newY] = dist[x][y] + 1
            q.append((newX, newY))

    if flag :
        break

print(1 if flag else 0)