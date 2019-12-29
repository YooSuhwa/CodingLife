'''
   @ ush 2019/12/29
   * 백준 알고리즘 - 13913 숨바꼭질4 (https://www.acmicpc.net/problem/13913)
   * python

   * 위치 n에서 k로 가는 가장 빠른 시간과 이동하는 방법을 구하는 문제
   * 1. 위치 x에서 할 수 있는 행동 : x+1 or x-1 or x*2 
   * 2. 세가지 행동 모두 1초로 동일. 따라서 BFS 이용
   * 3. way를 이용해 이동하는 방법(경로)를 기록.
    * way[next] = now   (next는 now에서 왔다)
    * 이때 way는 역순으로 저장되므로 go재귀함수를 통해서 역순으로 print 함
    * 재귀함수 제한 늘리기 위해 sys.setrecursionlimit() 사용. (런타임 에러 해결)
'''
import sys
MAX = 200000
sys.setrecursionlimit(MAX) #런타임에러 해결 (재귀 횟수 제한 늘리기)

def go(n,m):
    if n != m :
        go(n, way[m])
    print(m, end=" ")

n, m = map(int, input().strip().split(' '))

visit = [False]*MAX
dist = [-1]*MAX
way = [-1]*MAX

q = []
q.append(n)
visit[n] = True
dist[n] = 0
while q:
    now = q.pop(0)

    for i in range(0, 3):
        if i == 0 :
            next = now+1
            if next>=MAX or visit[next]:
                continue
        elif i == 1 :
            next = now-1
            if next<0 or visit[next]:
                continue
        elif i == 2 :
            next = now*2
            if next>=MAX or visit[next]:
                continue

        q.append(next)
        visit[next] = True
        dist[next] = dist[now] + 1
        way[next] = now

print(dist[m])
go(n, m)