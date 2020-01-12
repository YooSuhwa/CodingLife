/*
   @ 2019.01.12 ush
   * 백준 알고리즘 - 10942 팰린드롬? (https://www.acmicpc.net/problem/10942)
   * cpp

   * 문자열의 부분 수열이 팰린드롬인지 확인하는 문제
*/

#include <iostream>

using namespace std;

int N, M;
int dp[2001][2001];
int arr[2001];

int main() {
    cin >> N;
    
    for(int i = 1; i <= N; i ++)
        cin >> arr[i];
    
    for(int i = 1; i <= N; i ++)
        dp[i][i] = 1;
    
    for(int i = 1; i <= N-1; i ++) {
        if(arr[i] == arr[i+1])
            dp[i][i+1] = 1;
    }
    
    for (int i = 2; i <= N - 1; i++) {
        
        for (int j = 1; j <= N - i; j++) {
            if (arr[j] == arr[j + i] && dp[j + 1][j + i - 1]) {
                dp[j][j + i] = 1;
            }
        }
        
    }
    
    
    cin >> M;
    for(int i = 0; i < M; i ++) {
        int from, to;
        scanf("%d %d", &from, &to);
        cout<<dp[from][to]<<"\n";
    }
    return 0;
}

