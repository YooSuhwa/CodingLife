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

def bfs(num):
    q = deque()
    dist = [-1] * num
    way = [-1 ] * num
    how = [-1] * num

    temp = 1%num
    q.append(temp)
    dist[temp] = 0
    way[temp] = 0
    how[temp] = 1

    while q :
        now = q.popleft()
        for i in range(0,2):
            next = (now*10 + i)%num
            if dist[next] == -1:
                dist[next] = dist[now] +1
                way[next] = now
                how[next] = i
                q.append(next)

    if dist[0] == -1 :
        print("BRAK")
        return

    answer = ""
    i = 0
    while i!= -1:
        answer += str(how[i])
        i = way[i]
    print(answer)



testCase = int(input())
for _ in range(testCase):
    num = int(input())
    bfs(num)