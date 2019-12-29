'''
시간초과
'''
import sys
MAX = 10001
sys.setrecursionlimit(MAX)
def go(n,m):
    if n != m :
        go(n, way[m])
    print(how[m], end="")


test = int(input())
for _ in range(0, test):
    a, b = map(int, input().strip().split(" "))

    q = []
    visit = [False]*MAX
    dist = [-1]*MAX
    way = [-1]*MAX
    how = ['']*MAX

    q.append(a)
    visit[a] = True
    dist[a] = 0
    way[a] = 0
    while q :
        now = q.pop(0)
        for i in range(0, 4):
            if i == 0: #D
                next = int((now * 2) %10000)
                if visit[next] :
                    continue
                else :
                    how[next] = 'D'
            elif i == 1 : #S
                next = now - 1
                if next == 0 :
                    next = 9999
                if visit[next]:
                    continue
                else :
                    how[next] = 'S'
            elif i == 2 : #L
                next = int((now%1000)*10 +(now/1000))
                if visit[next]:
                    continue
                else :
                    how[next] = 'L'
            else : #R
                next = int((now %10)*1000 + (now/10))
                if visit[next] :
                    continue
                else :
                    how[next] = 'R'

            q.append(next)
            visit[next] = True
            dist[next] = dist[now]+1
            way[next] = now

    answer = ''
    go(a,b)
    print()