from collections import deque

n,m=map(int,input().split())

graph=[[0]*m for _ in range(n)]


for i in range(n):
    graph[i]=list(map(int,input().split()))

dx=[-1,1,0,0] 
dy=[0,0,-1,1]



def BFS(x,y):

    que=deque()
    que.append((x,y))
    
    visit[x][y]=1
    melt=deque()
    
    
    while(que):
        x,y=que.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0 and visit[nx][ny]==0:
                    visit[nx][ny]=1
                    que.append((nx,ny)) # 공기면 계속 탐색
                elif graph[nx][ny]==1 and visit[nx][ny]==0:
                    visit[nx][ny]=1
                    melt.append((nx,ny))
                    
    for x,y in melt:
        graph[x][y]=0 # 치즈 녹이기
        
    return len(melt)

cnt=0
time=1

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            cnt+=1          


    
while(1):
    visit = [[0] * m for _ in range(n)]
    
    melt_cnt=BFS(0,0)
    
    cnt-=melt_cnt
    
    if cnt==0:
        print(time,melt_cnt,sep='\n')
        break
    time+=1
    

# 2636 / Grpah,BFS
# 문제 설계를 깔끔하게 못해서 결국 풀지 못함
# 외곽을 탐색한다는 접근은 어느정도 맞았는데 
# 녹일 치즈를 담을 deque 를 하나 더 만들 생각을 못했음
# 첫번째 탐색 하는 경우 를 예시로 들면 공기인경우 -> 계속해서 주위에 치즈 탐색을 진행해야되므로 큐에 append
# 만약 치즈일경우 치즈의 좌표를 melt 에 넣어놓음
# melt 에 들어간 좌표는 녹아야될 치즈이기떄문에 0으로 변경해주고
# 녹은 치즈의 갯수를 반환함 
# 전체 치즈갯수에서 녹은 치즈갯수를 뺴줌 
# 아직 치즈가 남아있으면 다시 반복 진행!!!! 종료조건? 치즈가 0개!!!
# 다시 visit 배열 초기화하고 변경된 graph 에 대해 BFS 진행 
# 다시 공기면 탐색 , 치즈면 melt 에 모아두었다가 BFS 종료전에 녹여서 graph 변경시키고
# 밖에 나와서 녹은갯수만큼 빼주고 반복

https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2636-%EC%B9%98%EC%A6%88-BFS
