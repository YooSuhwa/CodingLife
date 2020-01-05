'''
   @ 2020.01.05 ush
   * 백준 알고리즘 -8111 0과 1 (https://www.acmicpc.net/problem/8111)
   * python

   * BFS

   * 자연수 N의 배수 중에서 다음 조건을 만족하는 가장 작은 수를 구하는 문제
    * 1. 0과 1로만 이루어져 있어야 한다.
    * 2. 1이 적어도 하나 있어야 한다.
    * 3. 수가 0으로 시작하지 않는다.
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

    how[temp] = 1

    while q :
        now = q.popleft()
        for i in [0,1]:
            next = (now*10 + i)
            next %= num
            if dist[next] == -1:
                dist[next] = dist[now] +1
                way[next] = now #from
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

    print(answer[::-1])

testCase = int(input())
for _ in range(testCase):
    num = int(input())
    bfs(num)