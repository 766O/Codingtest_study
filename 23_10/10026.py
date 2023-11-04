from collections import deque
import copy

N=int(input())

graph=[[0]*N for _ in range(N)]

visited=[[0]*N for _ in range(N)]
odd_visited=[[0]*N for _ in range(N)]

for i in range(N):
    graph[i]=list(input())
    
odd_graph=copy.deepcopy(graph)
for i in range(N):
    for j in range(N):
        if odd_graph[i][j]=='G':
            odd_graph[i][j]='R'

    
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def normal_BFS (x,y):
    que=deque()
    que.append((x,y))
    
    while que:
        x,y=que.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]==graph[x][y] and visited[nx][ny]==0:
                que.append((nx,ny))
                visited[nx][ny]=1

def odd_BFS (x,y):
    que=deque()
    que.append((x,y))
    
    while que:
        x,y=que.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<N and 0<=ny<N and odd_graph[nx][ny]==odd_graph[x][y] and odd_visited[nx][ny]==0:
                que.append((nx,ny))
                odd_visited[nx][ny]=1

    
normal_cnt=0
odd_cnt=0


for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            normal_BFS(i,j)
            normal_cnt+=1
            
for i in range(N):
    for j in range(N):
        if odd_visited[i][j]==0:
            odd_BFS(i,j)
            odd_cnt+=1


print(normal_cnt,odd_cnt)
    
# 10026 / BFS,Graph
# 내 풀이방법 -> 정상,색맹 에 따라 그래프를 다르게 만듬 
# 색맹사람의 그래프 (G 와 R 을 동일한색깔로 보니까 정상사람 그래프 에서 G 를 모두 R 로 바꿔줌)
# BFS 조건 (N*N 범위 내 이면서 , 이전에 방문하지 않았고 , 이전에 방문한 색깔값과 똑같아야함)
# 이떄 리스트를 복사해서 변경해서 만들려고함 -> copy 의 deepcopy 써야 원본에 영향이 없음
# 또는 다른방법으로 정상사람을 먼저 구한후 원본에서 G를 R로 바꾸고 BFS 실행하면 메모리를 더 쓰지 않아도 가능
