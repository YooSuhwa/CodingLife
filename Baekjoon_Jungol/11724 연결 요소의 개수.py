'''
   @ 2020/01/22 ush
   * 백준 알고리즘 - 11724 연결 요소의 개수 (https://www.acmicpc.net/problem/11724)
   * python (PyPy3)

   * dfs
   
'''
from collections import deque
def dfs(v, n):
    visit[v] = True

    for i in range(n):
        if vertex[v][i] == 1 and (not visit[i]) :
            dfs(i, n)


n, m = map(int, input().strip().split(' '))
vertex = [[0]* n for _ in range(n)]
for _ in range(m):
    u,v = map(int, input().strip().split(' '))
    u-=1
    v-=1
    vertex[u][v] = vertex[v][u] = 1

answer = 0
visit = [False] * n

for v in range(n):
    if visit[v] == False :
        answer +=1
        dfs(v, n)


print(answer)

