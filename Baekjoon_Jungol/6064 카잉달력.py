'''
   @ 2019.12.18 ush
   * 백준 알고리즘 - 6064 카잉 달력 (https://www.acmicpc.net/problem/6064)
   * python

   * 모든 경우의 수를 따지면 O(M*N), 즉 1600000000 가지임.
   * 따라서 x를 먼저 고정한 후 해당하는 y 찾는 방법으로 풀이
   * 1. year % M == x 인 year 중에서
   * 2. year % N == y 인 year 를 찾는 방

'''
def solution (M, N, x, y):
    x -= 1
    y -= 1

    year = x
    while year < M*N:

        if year % N == y :
            return year+1
        year += M


    return -1

def main():
    testCase = int(input())
    for _ in range(testCase):
        M, N, x, y = map(int, input().strip().split(' '))
        print(solution(M, N, x, y))

if __name__ == "__main__":
    main()