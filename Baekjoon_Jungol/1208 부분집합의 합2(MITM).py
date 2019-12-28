'''
   @ ush 2019/12/27
   * 백준 알고리즘 - 1208 부분수열의 합 2 (https://www.acmicpc.net/problem/1208)
   * python(PyPy3)

   * 부분수열 중 원소를 더한 값이 find가 되는 경우의 수 구하기
   * 배열의 크기인 n의 범위가 1~40으로 매우 크다. (2^40)
   * 따라서 MITM(meet in the middle)방법 사용
    * 배열을 반으로 나눠서 양쪽 절반에서 모든 경우를 다 해보는 방법.
   * 1. arr를 반으로 나눈다.
   * 2. 반으로 나눈 각 어레이의 모든 부분 수열의 합을 bitmask를 통해 담는다.
   * 3. team1(l)은 오름차순으로, team2(r)는 내림차순으로 정렬한다.
   * 4. sum = team1[l] + team2[r] 으로 계산한 후
   *    if sum > find : r-- (t2++)
        if sum < find : l++ (t1++)
        if sum == find : 갯수 찾아서 곱하고 더함. l++, r--
            중복수 건너뛰는거 주의
   * 5. find == 0 인 경우 공집합은 빼줘야 하므로 answer-- 하기
'''

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