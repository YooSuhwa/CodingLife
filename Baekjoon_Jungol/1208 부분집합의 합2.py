n,find = map(int,input().split())
arr = list(map(int,input().split()))

t2 = n//2
t1 = n - t2

team1 = [0]*(1<<t1)
team2 = [0]*(1<<t2)

for i in range(1<<t1) :
    for k in range(t1):
        if i&(1<<k) :
            team1[i] += arr[k]

for j in range(1<<t2) :
    for k in range(t2):
        if j&(1<<k) :
            team2[j] += arr[k+t1]

team1.sort()
team2.sort(reverse=True)
t1 = (1<< t1)
t2 = (1<< t2)
#[-10, -7, -3, 0] [13, 11, 8, 6, 5, 3, 0, -2]

i = j = 0
answer = 0

while i < t1 and j < t2:
    temp = team1[i] + team2[j]
    if temp > find :
        j+= 1
    elif temp < find :
        i+= 1
    else : # ==
        c1 = 1
        c2 = 1

        value = team1[i]
        i+= 1
        while i < t1 and value== team1[i]:
            c1+= 1
            i+= 1

        value = team2[j]
        j += 1
        while j < t2 and value == team2[j]:
            c2 += 1
            j += 1
        answer += (c1*c2)

if find == 0 :
    answer -= 1
print(answer)