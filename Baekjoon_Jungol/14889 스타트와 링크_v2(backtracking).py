'''
   @ 2019.12.22 ush
   * 백준 알고리즘 - 14889 스타트와 링크 (https://www.acmicpc.net/problem/14889)
   * python

   * backtracking

   * go(index, first, second)
   *    index번째 사람을 어떤 팀에 넣을지 결정.
   * index == N : 정답을 찾는 경우
   * len(team) > N/2 : 불가능한 경우
'''

def go(index, team1, team2, N, answer):
    if len(team1) > N/2 : return -1
    if len(team2) > N/2 : return -1

    t1 = 0
    t2 = 0
    if index == N: #끝
        for i in range(0, N//2):
            for j in range(0, N//2):
                t1 += stats[team1[i]][team1[j]]
                t2 += stats[team2[i]][team2[j]]

        return abs(t1-t2)


    #team1
    team1.append(index)
    now = go(index+1, team1, team2, N, answer)

    if (now != -1 and now < answer):
        answer = now
    team1.remove(index)

    #team2
    team2.append(index)
    now = go(index + 1, team1, team2, N, answer)

    if (now != -1 and now < answer):
        answer = now
    team2.remove(index)

    return answer

N = int(input())
stats = [list(map(int,input().split())) for _ in range(N)]
team = [0 if i < N/2 else 1 for i in range(N)]
answer = 1000000000
team1 = []
team2 = []

print(go(0, team1, team2, N, 100000))
