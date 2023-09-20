from collections import deque
N,M=map(int,input().split())

maze=[0 for _ in range(N)]

for i in range(N): 
    maze[i]=list(map(int,input()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def BFS(x,y):
    que=deque()
    que.append([x,y])
    
    while que:
        #import pdb;pdb.set_trace()
        x,y=que.popleft()
        
        for i in range (4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if maze[nx][ny]==1:
                que.append([nx,ny])
                maze[nx][ny]=maze[x][y]+1
            
                
BFS(0,0)
print(maze[N-1][M-1])

# 2178 / BFS
# 전형적인 미로문제 , 이코테 BFS 문제 (미로찾기) 와 동일
    
