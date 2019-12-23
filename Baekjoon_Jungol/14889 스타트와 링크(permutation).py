'''
   @ 2019.12.21 ush
   * 백준 알고리즘 - 14889 스타트와 링크 (https://www.acmicpc.net/problem/14889)
   * python

   * 순열을 이용한 브루트 포스
'''
def calculation (stats, team1, team2):
    t1 = 0
    t2 = 0
    for i in range(N//2):
        for j in range(N//2):
            if i == j : continue
            t1 += stats[team1[i]][team1[j]]
            t2 += stats[team2[i]][team2[j]]
    return abs(t1 - t2)
def nextPermutation(num):
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
        num[i],num[j] = num[j], num[i]
        i += 1
        j -= 1

    return True

N = int(input())
stats = [list(map(int,input().split())) for _ in range(N)]
team = [0 if i < N/2 else 1 for i in range(N)]
answer = 1000000000

while True :
    team1 = []
    team2 = []
    for i in range(N):
        if team[i] == 0:
            team1.append(i)
        else :
            team2.append(i)

    now = calculation(stats,team1, team2)
    if now < answer :
        answer = now
    if not nextPermutation(team) :
        break

print(answer)