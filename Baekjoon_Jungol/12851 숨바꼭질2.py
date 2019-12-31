'''
   @ ush 2019/12/31
   * 백준 알고리즘 - 12851 숨바꼭질4 (https://www.acmicpc.net/problem/12851)
   * python

   * BFS & DP

   * 위치 start에서 find로 가는 가장 빠른 시간과 그 시간으로 갈 수 있는 방법의 수를 구하는 문제
   * 가장 빠른 시간을 구하기 : BFS 이용 (dist, visit list)
   * 방법의 개수 구하기 : DP 이용 (count list)

'''
from collections import deque
MAX = 200001

start, find = map(int, input().strip().split(' '))

q = deque()
visit = [False]*MAX
dist = [-1]*MAX
count = [0]*MAX

q.append(start)
visit[start] = True
dist[start] = 0
count[start] = 1

while q :
    now = q.popleft()
    nextList  = [now-1, now+1, now*2]

    for next in nextList:
        if -1 < next < MAX:
            if not visit[next]:
                q.append(next)
                visit[next] = True
                dist[next] = dist[now] + 1
                count[next] = count[now]

            elif dist[next] == dist[now] + 1: #경우의 수 - DP
                count[next] += count[now]

print(dist[find])
print(count[find])