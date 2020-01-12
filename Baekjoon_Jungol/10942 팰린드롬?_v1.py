'''
   @ 2020/01/12 ush
   * 백준 알고리즘 - 10942 팰린드롬? (https://www.acmicpc.net/problem/10942)
   * python

   * dp
   * v1) top-down 방식

   * 어떤 수열의 부분수열이 팰린드롬인지 확인하는 문제

   * dp[i][j] = arr[i] ~ arr[j]가 팰린드롬이면 1, 아니면 0
   * 1. 길이가 1일 때 : 반드시 팰린드롬
   * 2. 길이가 2일 때 : 두수가 같으면 팰린드롬
   * 3. 그외 (3 이상)
        arr[i] == arr[j] 이고 arr[i+1]~arr[j-1]이 팰린드롬이여야 한다.
        즉, arr[i] == arr[j] and dp[i+1][j-1] = 1
'''
def go (start, end):
    if start == end : # 한글자
        return 1
    if start+1 == end : # 두글자
        if arr[start] == arr[end] :
            return 1
        return 0

    # 3글자 이상
    if dp[start][end] != -1 :
        return dp[start][end]
    if arr[start] != arr[end] :
        dp[start][end] = 0
        return 0
    dp[start][end] = go(start+1, end-1)
    return dp[start][end]



n = int(input())
arr = list(map(int, input().strip().split(" ")))
m = int(input())
quest = []
for _ in range(m):
    quest.append(list(map(int, input().strip().split(" "))))

dp = [[-1] * n for _ in range(n)]


for st, end in quest:
    print(go(st-1, end-1))