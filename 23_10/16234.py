from collections import deque

N,L,R=map(int,input().split())

country=[0]*N

for i in range(N):
    country[i]=list(map(int,input().split()))

visit=[[0]*N for _ in range(N)] 

que=deque()

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def BFS(que):
    
    tmp=0
    cnt=0
    flag=0
    union=[]
    # 초기데이터 
    x,y=que.popleft()
    visit[x][y]=1
    union.append([x,y])
    que.append([x,y])

    while que:
        
        #import pdb;pdb.set_trace()
        x,y=que.popleft()
        visit[x][y]=1
        
        

        
        for i in range(4): 
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            
            if abs(country[nx][ny] - country[x][y]) >=L and abs(country[nx][ny] - country[x][y]) <=R and visit[nx][ny]==0:
                visit[nx][ny]=1
                que.append([nx,ny]) # 조건 만족하는 애만 추가함 큐에 
                union.append([nx,ny])
        
    if len(union)>1:
        #print(union)
        temp=0
        cnt=len(union)
        for idx in union:
            x,y=idx
            temp+=country[x][y]
            data=temp//cnt
        
            
        for idx in union:
            x,y=idx
            country[x][y]=data
        
        return 1
        
    return 0 # 연합 없는경우
            
    

    
    
day=0

while 1:
    flag=0
    visit=[[0]*N for _ in range(N)] 
    for i in range(N): 
        for j in range(N): # 전체 돌면서
            if visit[i][j]==0: # 미방문지점에 대해 연합찾기
                que.append([i,j])
                t=BFS(que)
                if t==1: # 연합이 존재하는경우 
                    flag=1
    if flag==0: # 전체 탐색했는데도 연합이 존재 하지 않는경우
        break
        
    day+=1
    
print(day)
        
                            



