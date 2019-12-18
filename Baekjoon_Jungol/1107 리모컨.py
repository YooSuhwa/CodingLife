'''
   @ ush 2019/12/18
   * 백준 알고리즘 - 1107 리모컨 (https://www.acmicpc.net/problem/1107)
   * python

   1. 이동할 채널 channel 선택 (0~100,000)
   2. channel에 포함되어 있는 숫자 중에 고장난 버튼이 있는지 확인 - isNotBroken()
   3. 고장난 버튼이 포함되어 있지 않다면, 'channel의 자릿수(숫자 버튼 갯수) + channel에서 target으로 가는 차이' 를 계산
   4. min(channel, channelLength + abs(target - channel))
'''

def isNotBroken (c, broken):
    if c == 0 :
        if '0' in broken:
            return 0
        else:
            return 1

    channel = str(c)
    for cc in channel:
        if cc in broken:
            return 0
    return len(channel)

broken = []
currentMin = 0

target = int(input())
brokenLength = int(input())

if brokenLength>0 :
    broken = list(map(str,input().split()))

currentMin = abs(target - 100)

for channel in range(0, 1000000):
    channelLength = isNotBroken(channel, broken)
    if channelLength != 0 : #아무것도 브로큰 없으면
        channel = channelLength + abs(target - channel)
        currentMin = min(channel, currentMin)

print(currentMin)


