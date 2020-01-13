'''
   @ 2020/01/13 ush
   * 백준 알고리즘 - 15989 1,2,3 더하기 4 (https://www.acmicpc.net/problem/15989)
   * python

   * dp
   
   * 정수 n을 1,2,3의 합으로 나타내는 방법의 수를 구하는 문제
   * 이때 합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 친다
    * 즉, 중복 제외 (2+1+1 == 1+1+2 == 1+2+1)
    * '9095 1,2,3 더하기' 문제와 다른점
   * dp[i] = i를 1,2,3의 조합으로 나타내는 방법의 수
    * dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        * dp [i-1] : 맨 마지막에 1이 오는 경우
        * dp [i-2] : 맨 마지막에 2가 오는 경우
        * dp [i-3] : 맨 마지막에 3이 오는 경우
'''
testcase = int(input())

for _ in range(testcase):
    n = int(input())
    dp = [0] * (n+1)

    size = 3
    seq = (1,2,3)
    dp[0] = 1

    for i in range(0, size):
        for j in range(1, n+1):
            if j-seq[i] >= 0:
                dp[j] += dp[j - seq[i]]

    print(dp[n])