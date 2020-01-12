'''
   @ 2020/01/12 ush
   * 백준 알고리즘 - 10942 팰린드롬? (https://www.acmicpc.net/problem/10942)
   * python

   * dp
   * v2) bottom-up 방식

   * 어떤 수열의 부분수열이 팰린드롬인지 확인하는 문제

   * dp[i][j] = arr[i] ~ arr[j]가 팰린드롬이면 1, 아니면 0
   * 1. 길이가 1일 때 : 반드시 팰린드롬
   * 2. 길이가 2일 때 : 두수가 같으면 팰린드롬
   * 3. 그외 (3 이상)
        arr[i] == arr[j] 이고 arr[i+1]~arr[j-1]이 팰린드롬이여야 한다.
        즉, arr[i] == arr[j] and dp[i+1][j-1] = 1
'''
n = int(input())
arr = list(map(int, input().strip().split(" ")))
m = int(input())
quest = []
for _ in range(m):
    quest.append(list(map(int, input().strip().split(" "))))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1
for k in range(3, n+1):
    for start in range(0, n-k+1):
        end = start + k - 1
        if arr[start] == arr[end] and dp[start+1][end-1]:
            dp[start][end] = 1

for st, end in quest:
    print(dp[st-1][end-1])