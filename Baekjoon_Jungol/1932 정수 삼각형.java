/*
	@ 2020.01.03 ush
	* 백준 알고리즘 - 1932 정수 삼각형 (https://www.acmicpc.net/problem/1932)
	* java
	
	* 삼각형의 맨 위층부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려온다.
	* 이때 전체 선택된 수의 합이 최대가 되는 경로를 구하기
	* 단, 선택된 수의 대각선 왼쪽 혹은 대각선 오른쪼겡 있는 것중에서만 선택할 수 있다.
*/
#include <stdio.h>
void inputNum(int);
int intTriangle(int);

int num[500][500]={};
int main(){
    int size;
    
    scanf("%d", &size);
    
    inputNum(size);
    printf("%d", intTriangle(size));
 
    
}
void inputNum (int size){
    for (int i =0; i <size; i++) {
        for (int j = 0; j < i+1; j++) {
            scanf("%d", &num[i][j]);
        }
    }
}

int intTriangle(int size){
    int n1, n2;
    
    
    for (int i = 1; i<size; i++) {
        for (int j = 0; j < i+1; j++) {
            if(j == 0){
                num[i][j] = num[i-1][j]+num[i][j];
            }
            else{
                n1 = num[i-1][j-1];
                n2 = num[i-1][j];
                
                if(n1>n2){
                    num[i][j] = n1+num[i][j];
                }else{
                     num[i][j] = n2+num[i][j];
                }
            }
        }
    }
    
    int max = num[size-1][0];
    for (int i = 1; i < size; i++) {
        if(max < num[size-1][i]){
            max =num[size-1][i];
        }
    }
    
    
    return max;
}

