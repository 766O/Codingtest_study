N=int(input())

stair=[0]* 301

for i in range(N):
    stair[i]=int(input())

dp=[0]*301

dp[0]=stair[0]
dp[1]=stair[0]+stair[1]
dp[2]=max((stair[0]+stair[2]),(stair[1]+stair[2]))

for i in range(3,N):
    dp[i]=max(dp[i-3]+stair[i-1]+stair[i] , dp[i-2]+stair[i])

print(dp[N-1])

# 2579 / DP
# 점화식 찾기....
# 작은케이스로 변경후에 이전에 나온 값으로 치환 할 수 있는것을 치환해보자]
# 또한 문제에서는 최대값이 나오는 경우만을 물어보고 있으니까 
# 모든 계단 오르는 수를 고려할 필요가 없음 
# 즉 이전 단계의 최대값을 가져와서 
