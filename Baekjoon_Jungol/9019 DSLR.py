'''
   @ ush 2019/12/29
   * 백준 알고리즘 - 9019 DSLR (https://www.acmicpc.net/problem/9019)
   * python

   * BFS

   * 네자리 숫자 A, B가 주어졌을 때 A에서 B로 바꾸는 최소 연산 횟수와 과정을 구하는 문제
   * D, S, L, R 네가지 행동을 할 수 있다.
    * 이때 네가지 행동 모두 중요도가 같으므로 BFS를 이용
    
   * 주의 !!!! deque안쓰고 q.pop(0)을 사용했는데 시간초과가 떴음   
'''
from collections import deque
import sys
MAX = 10001
sys.setrecursionlimit(MAX)

test = int(input())
for _ in range(0, test):
    a, b = map(int, input().strip().split(" "))

    q = deque()
    visit = [False]*MAX
    dist = [-1]*MAX
    way = [-1]*MAX
    how = ['']*MAX

    q.append(a)
    visit[a] = True
    dist[a] = 0
    way[a] = 0
    while q :
        now = q.popleft()
        for i in range(0, 4):
            if i == 0: #D
                next = (now*2) % 10000
                if visit[next] :
                    continue
                else :
                    how[next] = 'D'
            elif i == 1 : #S
                next = now - 1
                if next == -1 :
                    next = 9999
                if visit[next]:
                    continue
                else :
                    how[next] = 'S'
            elif i == 2 : #L
                next = (now%1000)*10 +(now//1000)
                if visit[next]:
                    continue
                else :
                    how[next] = 'L'
            else : #R
                next = (now %10)*1000 + (now//10)
                if visit[next] :
                    continue
                else :
                    how[next] = 'R'

            q.append(next)
            visit[next] = True
            dist[next] = dist[now]+1
            way[next] = now

    answer = ''
    while a!= b:
        answer += how[b]
        b = way[b]
    print(''.join(reversed(answer)))