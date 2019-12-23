/*
   @ 2019.12.23 ush
   * 백준 알고리즘 - 2580 스도쿠 (https://www.acmicpc.net/problem/2580)
   * python

   * 스도쿠에서 만족해야 할 3가지 조건
   * 1. 각 행에는 0-9가 하나씩 들어가야 한다 << checkRow로 확인
   * 2. 각 열에는 0-9가 하나씩 들어가야 한다 << checkLow로 확인
   * 3. 3*3 사각형에는 0-9가 하나씩 들어가야 한다. << checkSq로 확인

*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
using namespace std;

int n = 9;
int sudoku[10][10] ={0,};
bool checkRow[10][9] = {false,};
bool checkCol[10][9] = {false,};
bool checkSq[10][9] = {false,};

int findSq(int r, int c){
    return int((r/3))*3 + int((c/3));
}
void printSudoku(){
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cout << sudoku[i][j] << ' ';
        }
        cout << '\n';
    }
    
}
void goSudoku(int index, int N){
    if (index == N){
        printSudoku();
        exit(0);
    }
    int row = index / n;
    int col = index % n;
    
    if (sudoku[row][col] != 0) {
        goSudoku(index+1, N);
    }
    else{
        for (int i = 1; i <n+1; i++){
            if (checkRow[row][i] == false && checkCol[col][i] == false&& checkSq[findSq(row, col)][i] == false){
                sudoku[row][col] = i;
                checkRow[row][i] = true;
                checkCol[col][i] = true;
                checkSq[findSq(row, col)][i] = true;
                
                goSudoku(index+1, N);
                
                sudoku[row][col] = 0;
                checkRow[row][i] = false;
                checkCol[col][i] = false;
                checkSq[findSq(row, col)][i] = false;
                
            }
        }
    }
}

int main() {
    int N = n*n;
    
    int num = 0;
    for (int row=0; row<n; row++) {
        for (int col=0; col<n; col++) {
            cin >> num ;
            sudoku[row][col] = num;
            if (num != 0) {
                checkRow[row][num] = true;
                checkCol[col][num] = true;
                checkSq[findSq(row, col)][num] = true;
            }
        }
    }
    goSudoku(0, N);
    cout << "finish";
    return 0;
}
