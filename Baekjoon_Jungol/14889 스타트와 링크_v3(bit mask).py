'''
   @ 2019.12.23 ush
   * 백준 알고리즘 - 14889 스타트와 링크 (https://www.acmicpc.net/problem/14889)
   * python

   * bit mask

   * N명을 두 팀 중 하나로 나누는 문제이므로 비트 마스크를 이용. 
   * 1. n개의 0으로 이루어진 이진수 부터 n개의 1로 이루어진 이진수까지 범위로 for문 실행
   * 2. bitmask(i&2<<j) 를 통해서 나눠지는 팀원의 갯수를 count한다
   * 3. 만약 팀이 반씩 나눠졌다면 (count == N//2), 그대로 팀을 나눈 후 팀 능력치 차이를 계산한다.
   * 4. 두팀으로 나눠지는 모든 능력치 차이를 계산하면서 최소값을 찾는다.

'''

def computeDiffer (team1, team2):
    t1 = 0
    t2 = 0

    for i in range(0, N//2):
        for j in range(0, N//2):
            t1 += stats[team1[i]][team1[j]]
            t2 += stats[team2[i]][team2[j]]

    return abs(t1 - t2)


N = int(input())
stats = [list(map(int,input().split())) for _ in range(N)]
team = [0 if i < N/2 else 1 for i in range(N)]
answer = 1000000000

final = 1 << N

for i in range(0, final):
    count = 0

    for j in range(0, N):
        if i&(1<<j) :
            count += 1

    if count != N//2 :
        continue

    team1 = []
    team2 = []
    for j in range(0, N):
        if i&(1<<j) :
            team1.append(j)
        else :
            team2.append(j)

    now = computeDiffer(team1, team2)
    if now < answer:
        answer = now

print(answer)