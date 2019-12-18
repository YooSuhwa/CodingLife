/*
   @ ush 2019/12/18 
   * 백준 알고리즘 - 1107 리모컨 (https://www.acmicpc.net/problem/1107)
   * cpp

   1. 이동할 채널 channel 선택 (0~100,000)
   2. channel에 포함되어 있는 숫자 중에 고장난 버튼이 있는지 확인 - isNotBroken()
   3. 고장난 버튼이 포함되어 있지 않다면, 'channel의 자릿수(숫자 버튼 갯수) + channel에서 target으로 가는 차이' 를 계산
   4. min(channel, channelLength + abs(target - channel))
*/
#include <iostream>
using namespace std;

int broken[10];
int isNotBroken(int c){
    int ch = 0, len = 0;
    if (c == 0) {
        if (broken[0] == 1){
            return 0;
        }
        else{
            return 1;
        }
    }
    while(c > 0){
        ch = c%10;
        if (broken[ch] == 1){
            return 0;
        }
        len +=1;
        c /= 10;
    }
    return len;
    
}
int main() {
    int target =0, brokenLength = 0;
    int currentMin = 0;
    
    cin >> target;
    cin >> brokenLength;
    
    for (int i = 0; i < brokenLength; i++){
        int x = 0;
        cin >> x;
        broken[x] = 1;
    }
    
    currentMin = abs(target- 100);
    for (int channel = 0 ; channel <= 1000000; channel++){
        int channelLength = isNotBroken(channel);
        if (channelLength > 0){
            int temp = channelLength + abs(target - channel);
            currentMin = min(temp, currentMin);
        }
    }

    printf("%d\n", currentMin);
        
    return 0;
}

