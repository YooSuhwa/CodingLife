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

