import sys

input=sys.stdin.readline

N=int(input())
cnt=0

dp=[[0]*10 for _ in range(N+1)]

dp[1]=[1,1,1,1,1,1,1,1,1,1]

for i in range(2,N+1):
    for j in range(10):
        cnt=0
        for k in range(j,10):
            cnt=cnt+dp[i-1][k]
        
        dp[i][j]=cnt
    
  
print(sum(dp[N])%10007)

'''
11057 / DP

점화식은 상당히 빨리 찾았는데 찾은 점화식을 코드로 구현할때 시간이 좀 걸렸음 

다만 삼중반복문으로 구현했는데 올바른 코드 구현은 아닌듯

아래는 정석 풀이
'''  

import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * 10 # n=1 일때 오르막수 

for i in range(n-1): # n 개에 대한 경우를 차례차례 해결해나감
    for j in range(1, 10): # 0~9 번 인덱스에 저장되어있는 값들을 더해나감 
        dp[j] += dp[j-1]

print(sum(dp) % 10007)
