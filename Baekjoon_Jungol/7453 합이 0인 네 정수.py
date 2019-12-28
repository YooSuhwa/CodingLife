import sys
n = int(input())
temp = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
a,b,c,d = zip(*temp)

teamAB = []
teamCD = []
answer = 0


for i in range(n):
    for j in range(n):
        teamAB.append(a[i]+b[j])
        teamCD.append(c[i]+d[j])

for num in teamAB:
    answer += teamCD.count(-num)

print(answer)