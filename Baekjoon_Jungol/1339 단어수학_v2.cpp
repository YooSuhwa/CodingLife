'''
   @ 2019.12.21 ush
   * 백준 알고리즘 - 1339 단어수학 (https://www.acmicpc.net/problem/1339)
   * cpp

   * 만들 수 있는 합의 '최대값'만 구하면 되므로 순열을 이용한 브로드포스 방법
   * 1. 연산 알파벳을 입력을 받으면 집합을 통해 필요한 알파벳의 갯수를 알아냄 (중복제거)
   * 2. 중복이 제거된 알파벳이 k개라면, 9876... 순으로 k개를 넣어 순열을 이용해 계산
   * 3. 계산된 값들 중 최대값을 찾는다.

'''
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
using namespace std;

int calculation (vector<string> &calcul, vector<char> &letters, vector<int> &numbers){
    int sum = 0;
    int size = letters.size();
    char dict[256];
    
    for (int i = 0; i < size; i++){
        dict[letters[i]] = numbers[i];
    }
    for (string cal :  calcul){
        int now = 0;
        for ( char c : cal){
            now = now *10 + dict[c];
        }
        sum += now;
    }
    
    return sum;
}
int main() {
    int N = 0, answer = 0, size = 0, num = 0;
    cin >> N;
    
    vector<string> calcul(N);
    vector<char> letters;
    vector<int> numbers;
    

    for (int i = 0; i < N; i++){
        cin >> calcul[i];
        for (char c : calcul[i]){
            letters.push_back(c);
        }
    }
    sort(letters.begin(), letters.end());
    letters.erase(unique(letters.begin(), letters.end()), letters.end());
    
    size= letters.size();
    
    for (int i = 0; i <size; i++){
        numbers.push_back(9-i);
    }
    
    
    while (1){
        num = calculation(calcul, letters, numbers);
        if (num > answer) {
            answer = num;
        }
        if (!prev_permutation(numbers.begin(), numbers.end())){
            break;
        }
    }
    
    cout << answer;
        
    return 0;
}
