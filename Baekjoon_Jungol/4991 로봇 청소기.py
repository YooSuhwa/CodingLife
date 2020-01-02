'''
   @ 2020.01.02 ush
   * 백준 알고리즘 - 4991 로봇 청소기 (https://www.acmicpc.net/problem/4991)
   * python

   * BFS

   * 모든 더러운 칸을 깨끗한 칸으로 바꾸기 위해 필요한 최소 이동 횟수 구하는 문제
   * 더러운 칸을 정점이라고 봤을 때, 두 정점간의 최단 거리를 구하며 한칸씩 이동(가중치 1)하므로 BFS이용
   * 단, 찾아가는 더러운 칸의 순서에 때라 최단거리가 달라질 수 있다. <- 순열을 이용 
'''
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


def next_permutation(num):
    i = len(num)-1
    while i > 0 and num[i-1] >= num[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(num)-1
    while num[j] <= num[i-1]:
        j -= 1

    num[i-1],num[j] = num[j],num[i-1]

    j = len(num)-1
    while i < j:
        num[i],num[j] = num[j],num[i]
        i += 1
        j -= 1

    return True


dx = [0,0,-1,1]
dy = [-1,1,0,0]
while True :
    w, h = map(int, input().strip().split(' '))
    if w == 0 and h == 0 :
        break
    board = [input() for _ in range(h)]
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

    for i in range(0, length):
        distEach = bfs(q[i][0], q[i][1])
        for j in range (0, length):
            dist[i][j] = distEach[q[j][0]][q[j][1]]
            if dist[i][j] == -1 :
                flag = -1
                break

    if flag == -1 :
        print(-1)
        continue

    permutation = [i+1 for i in range(0, length-1)]

    answer = -1
    while True :
        now = dist[0][permutation[0]]

        for i in range(length-2):
            now += dist[permutation[i]][permutation[i+1]]

        if answer == -1 or answer > now :
            answer = now
        if not next_permutation (permutation):
            break

    print(answer)