from collections import deque

N,M=map(int,input().split())

graph=[[0]*M for _ in range(N)]
visit=[[0]*M for _ in range(N)]

for i in range(N):
    graph[i]=list((input()))
    
dx=[-1,1,0,0]
dy=[0,0,-1,1]

global result
cnt=0    
    
def BFS(x,y,cnt):
    que=deque()
    que.append((x,y))
    visit[x][y]=1
    
    while que:
        x,y=que.popleft()
        if graph[x][y]=='P':
            cnt+=1
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<N and 0<=ny<M and visit[nx][ny]==0 and graph[nx][ny]!='X':
                que.append((nx,ny))
                visit[nx][ny]=1
                
    return cnt


for i in range(N):
    for j in range(M):
        if graph[i][j]=='I':
            result=BFS(i,j,cnt)
if result==0:
    print('TT')
else:
    print(result)

# 21736 / BFS
# 기본 BFS 유형 문제            
