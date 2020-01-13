'''
   @ 2020/01/13 ush
   * 백준 알고리즘 - 9095 1,2,3 더하기 (https://www.acmicpc.net/problem/9095)
   * python

   * dp
   
   * 정수 n을 1,2,3의 합으로 나타내는 방법의 수를 구하는 문제
'''
testcase = int(input())

for _ in range(testcase):
    n = int(input())
    dp = [0] * (n+1)

    size = 3
    seq = (1,2,3)
    dp[0] = 1

    for j in range(1, n + 1):
        for i in range(0, size):
            if j-seq[i] >= 0:
                dp[j] += dp[j - seq[i]]

    print(dp[n])