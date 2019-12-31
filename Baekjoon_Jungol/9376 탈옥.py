'''
   @ 2019.12.31 ush
   * 백준 알고리즘 - 9376 탈옥 (https://www.acmicpc.net/problem/9376)
   * python

   * BFS
   
   * 두 죄수가 탈옥하기 위해서 열어야 하는 문의 최소 개수를 구하는 문제
   * 1. 일반적인 BFS는 하나의 시작점 -> 하나의 도착점이다. 
        따라서 두 죄수를 따로 나누어 BFS를 각각 구한다
   * 2. 하나의 도착점을 두기 위해서 기존 지도의 테두리를 1칸씩 빈칸으로 확장한다
   * 3. BFS의 가중치를 계산할 때 
        문을 지나면 (빈칸>>문) 가중치를 1로 두고 q.push_back
        문을 지나지 않으면 (빈칸>>빈칸 or 문>>빈칸) 가중치 0으로 두고 q.push_front
   * 4. 각 죄수에 대한 bfs와 도착점 (보드 밖, 즉 확장한 테두리 point중 하나)에서의 bfs를 각각 구한다.
   * 5. 위에서 구한 3개의 bfs를 합쳐 답을 구한다.
    * 문에서 만나는 경우에는, 문은 한번만열어야 하는데 현재 3개의 bfs에서 모두 연 상황이므로 -2 를 해야한다.
'''
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

    # bfs0 : from external point (0,0)
    bfs0 = makeBFS(board, 0, 0, h, w)

    # 죄수위치 찾기
    flag = -1
    for i in range(h):
        for j in range(w):
            if board[i][j] == '$':  # prisoner
                if flag == -1:
                    x1 = i
                    y1 = j
                    flag = 1
                else:
                    x2 = i
                    y2 = j
                    break

    # bfs1 : prisoner1 / bfs2 : prisoner2
    bfs1 = makeBFS(board, x1, y1, h, w)
    bfs2 = makeBFS(board, x2, y2, h, w)

    answer = h * w
    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                continue
            temp = bfs0[i][j] + bfs1[i][j] + bfs2[i][j]
            if board[i][j] == '#':
                temp -= 2

            answer = min(answer, temp)

    print(answer)