from collections import deque

n,m=map(int,input().split())

matrix=[[0]*m for _ in range(n)]

for i in range(n):
    matrix[i]=list(map(int, input().split()))
    
    
visit=[[0]*m for _ in range(n)]

    
que=deque()

dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0

def BFS(que):
    global cnt
    
    while que:
        #import pdb;pdb.set_trace()
        
        x,y=que.popleft()
        
       
        
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx>=0 and nx<n and ny>=0 and ny<m and visit[nx][ny]==0 and matrix[nx][ny]==1:
                matrix[nx][ny]=matrix[x][y]+1
                visit[nx][ny]=1
                que.append((nx,ny))


for i in range (n):
    for j in range(m):
        if matrix[i][j]==2:
            que.append((i,j))
            matrix[i][j]=0       
BFS(que)

for i in range(n):
    for j in range(m):
        if visit[i][j] == False and matrix[i][j]!=0:
            matrix[i][j] = -1
        
#print(matrix)

for i in range(n):
    
    for j in range(m):
        print(matrix[i][j],end=' ')
    print("")
    
# 14940 / BFS
# 문제에서 요구하는 BFS 함수는 잘 작성했음
# visit 함수 추가 + 카운트는 이전의 matrix 의 값을 가져와서 1더해줌
# 하지만 문제에서 언급한 예외 조건을 이해하지 못했다
# 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다. -> 1이면 갈 수 있지만 목표지점이 0 으로 둘러싸인경우 목표지점 도달을 못한다는 뜻
# 이 경우에 1이었던 판을 전부 -1 로 바꿔야함 
# 출력형식!!!! 아무생각없이 그대로 출력하지 말자!!!
