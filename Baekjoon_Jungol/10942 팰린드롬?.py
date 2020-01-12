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