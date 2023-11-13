from collections import deque

N=int(input())

graph=[[0]*N for _ in range(N)]

for i in range(N):
    graph[i]=list(map(int,input().split()))

global white
global blue

def check(x,y,n): # 시작좌표에서 n 만큼 가로 세로 찾아야함 
    color=graph[x][y] # 시작좌표의 색깔 받아놓고 
    for i in range(x,x+n): # 시작좌표에서 가로,세로만큼 모두 색깔이 같은지 검사
        for j in range(y,y+n):
            if color!=graph[i][j]: 
                return -1 # 만약 색이 다른경우 -1 반환
            
    return color # 만약 해당 영역이 모두 같은 색이라면 
                # 흰색인지 파란색인지 따라서 1 또는 0 반환 

def solve(x,y,n):
    global white
    global blue
    
    if check(x,y,n)==-1: # 만약 검사 영역 내 색이다른경우가 존재한다면 
                        # 총 4 가지 구역 , 영역은 절반으로 줄여서 다시 검사
        solve(x,y,n//2) # 똑같은 시작위치 , 영역 절반
        solve(x+n//2 , y , n//2) # 기존 시작위치에서 절반 y 방향 아래로 가서 영역 절반 검사
        solve(x , y+n//2 , n//2) # 기존 시작위치에서 절반 x 방향 오른쪽으로 가서 영역 절반 검사
        solve(x+n//2 , y+n//2 , n//2) # 기존 시작위치에서 절반 x,y 방향으로 가서 영역 절반 검사
    elif check(x,y,n) == 1: # 만약 모든 영역이 파란색인경우 
        blue+=1 # 파란색 케이스 추가
    else: # 만약 모든영역이 흰색인 경우
        white+=1 # 흰색 케이스 추가

blue=0
white=0

solve(0,0,N)

print(white)
print(blue)

#
    
        
    


