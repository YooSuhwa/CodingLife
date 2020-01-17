'''
   @ 2020/01/17 ush
   * 백준 알고리즘 - 11058 크리보드 (https://www.acmicpc.net/problem/11058)
   * python

   * dp

   * 버튼 4가지 종류
   		* 1. 화면에 A를 출력한다
   		* Ctrl-A: 화면을 전체 선택한다
   		* Ctrl-C: 전체 선택한 내용을 버퍼에 복사한다
   		* Ctrl-V: 버퍼가 비어있지 않은 경우에는 화면에 출력된 문자열의 바로 뒤에 버퍼의 내용을 붙여넣는다.
   * 이때 버튼을 총 N번 눌러서 화면에 출력되는 A의 최대 개수 구하는 코드

   * dp[i] = 버튼 i번 눌렀을때 화면에 출력된 A 최대 개수
   * 1번 버튼을 누르면 dp[i] = dp[i-1]+1
   * 2>>3>>4버튼 순서대로 누르면 dp [i] = dp[i-3]*2
   * 2>>3>>4>>4 순서대로 누르면 dp [i] = dp[i-4]*3
   * 2>>3>>4>>4>>4 순서대로 누르면 dp [i] = dp[i-5]*4
   * >> 일반화 ! 2>>3누르고 4번(ctrlV)버튼을 j 번 누른 경우 dp[i-(j+2)] * (j+1)

   * dp[i] = max(dp[i-1]+1 , dp[i-(j+2)] * (j+1)) 
   		* i <= j <= i-3
'''
n = int(input())
n+=1
dp = [-1]*n
dp[0] = 0
for i in range(1,n):
    dp[i] = dp[i-1]+1
    for j in range(1,i-2):
        temp = dp[i-(j+2)]*(j+1)
        dp[i] = max(dp[i], temp)
print(dp[n-1])