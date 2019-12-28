from collections import Counter

find = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

team1 = []
team2 = []

#부 배열은 연속된거!!!!! 따라서 bit마스크 안썼음
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += a[j]
        team1.append(temp)

for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += b[j]
        team2.append(temp)

team1.sort()
team2.sort()

counter = Counter(team2)

answer = 0
for num in team1:
    temp = find - num
    answer += counter[temp]

print(answer)