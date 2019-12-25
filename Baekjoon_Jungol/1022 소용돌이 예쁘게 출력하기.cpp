/*
   @ 2019.12.25 ush
   * 백준 알고리즘 - 1022 소용돌이 예쁘게 출력하기 (https://www.acmicpc.net/problem/1022)
   * cpp

   * r2 - r1 +1개의 줄에 소용돌이를 출력한다.
   * 이때 0행 0열에 숫자 '1'을 쓴 후 소용돌이는 반시계 방향으로 돌아가며 숫자를 입력한다.
   * 모든 숫자의 길이(앞에 붙는 공백 포함)는 같아야 한다.
     따라서 수를 입력하면서 가장 큰 수 max를 찾고 그 수의 자릿수를 확인 한 후 출력한다.

*/
#include <iostream>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

int arr[49][49] = {1,};
int maxDigit(int max){
    int digit = 0;
    
    while(max > 0){
        digit++;
        max /= 10;
    }
    return digit;
}
void vortex(int r1, int c1, int r2, int c2){
    
    int x = 0, y = 0;
    int digit = 0, max = -1;
    int size = (r2 - r1 + 1) * (c2 - c1 + 1);
    
    for (int i = r1; i <= r2; i++) {
        for( int j = c1; j <= c2; j++){
            x = i - r1;
            y = j - c1;
            
            if(i==j){
                if(i<0){
                    arr[x][y] = pow((i * 2),2) + 1;
                }else{
                    arr[x][y] = pow((i * 2+1), 2);
                }
            }else if(i>j){
                if(i>-j){
                    arr[x][y] = pow((i*2+1), 2) - i + j;
                    
                }else{
                    arr[x][y] = pow((j*2), 2) + i - j + 1;
                }
            }else if(i<j){
                if (i>-j){
                    arr[x][y] = pow((j * 2 - 1), 2) - i + j;
                }else {
                    arr[x][y] = pow((i * 2), 2) + i - j +1;
                }
            }
            
            if(max < arr[x][y]){
                max = arr[x][y];
            }
        }
    }
    digit = maxDigit(max);
    
    for (int i = r1; i <= r2; i++) {
        for( int j = c1; j <= c2; j++){
            x = i - r1;
            y = j - c1;
            cout << setw(digit)<< arr[x][y] << " ";
        }
        cout<<"\n";
    }
}
int main() {
    int r1 = 0, c1 = 0, r2 = 0, c2 = 0;
    cin >> r1 >> c1 >> r2 >> c2;
    
    vortex(r1, c1, r2, c2);
    return 0;
}
