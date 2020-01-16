/*
   @ 2020.01.16 ush
   * 백준 알고리즘 - 1932 정수 삼각형 (https://www.acmicpc.net/problem/1932)
   * cpp

   * 정수로 이루어진 삼각형의 
     맨 위층에서 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
     이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램

*/
#include <iostream>
using namespace std;

void inputNum(int);
int intTriangle(int);

int num[500][500]={};
int main(){
    int size;
    
    cin >> size;

    inputNum(size);
    cout<<intTriangle(size)<<"\n";
 
}
void inputNum (int size){
    for (int i =0; i <size; i++) {
        for (int j = 0; j < i+1; j++) {
            cin >>num[i][j];
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

