from collections import deque

n,m=map(int,input().split())

graph=[[0]*m for _ in range (n)]
tmp=[[999]*m for _ in range (n)]

for i in range(n):
    graph[i]=list(map(int,input().split()))



    
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,1,-1,1,-1]

def BFS(x,y):
    visit=[[0]*m for _ in range (n)]
    que=deque()
    que.append((x,y))
    visit[x][y]=1
    
    while que:
        x,y=que.popleft()
        
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if visit[nx][ny]==0:
                    visit[nx][ny]=visit[x][y]+1
                    
                    que.append((nx,ny))
    
    for i in range (n):
        for j in range(m):
            if visit[i][j] < tmp[i][j]:
                tmp[i][j]=visit[i][j]
        

    

    

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            BFS(i,j)
            
print(max(map(max, tmp))-1)
    
# 17086 / BFS
# 2주만의 코테준비 다시 시작 , 재활문제
# 내가 푼 방법은 상어가 위치한 지점 1에서 전 지점에 대해 BFS를 돌린다
# 해당 1 지점에서 BFS 돌린결과가 visit 에 담겨있게 되고 
# tmp 배열은 매우큰수로 처음에 초기화 돼있으므로 처음 visit 결과가 tmp에 담기게 된다
# 다음 1 지점이 존재 한다면 해당 지점에서 BFS 돌린결과가 visit 에 새로 담기게 된다
# 이때 이전의 BFS 결과인 tmp 와 비교해서 만약 더 최단거리가 있으면 tmp 를 업데이트한다
# 위 방법을 계속 반복하면 모든 1 지점에 대해 최단거리 들만이 tmp 에 남게된다.
# 그 중에서 가장 큰 숫자를 max(map(max, tmp))-1  를 통해 구한다

# 다른사람 풀이법
#  if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]: 
# 해당 구간 범위 내이면서 아직 방문을 하지 않았고 
#  graph[nx][ny] == 0    graph 값이 0 이라면 
#  que.append((nx, ny, distance+1)) que 에 해당 지점과 거리를 1 추가해서 큐에 저장 후
#  visited[nx][ny] = True 방문표시
#  else: return distance+1  만약 graph 값이 1이라면 거리 return
'''
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            ans = max(ans, bfs(i, j))
모든 0 인지점에 대해 BFS
'''
    
