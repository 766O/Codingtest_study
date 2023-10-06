from collections import deque

c,r,t=map(int,input().split())

graph=[[0]*r for _ in range(c)]
visit=[[0]*r for _ in range(c)]

print(graph)

for i in range(c):
        graph[i]=list(map(int,input().split()))
        


# 확산 함수
def BFS(x,y):
    que=deque()
    que.append((x,y))

    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    while que:
        possible=[]
        x,y=que.popleft()
        visit[x][y]=1
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx>=0 and nx<c and ny>=0 and ny<r and graph[nx][ny] != -1 :
                pass_dust=graph[x][y]//5
                
                tmp_graph[nx][ny]+=pass_dust
                tmp_graph[x][y]=tmp_graph[x][y]-pass_dust 


# possible 에 추가한다는거 자체가 이미 조건을 만족한것 그렇다면 그냥 조건문안에서 처리하면 됨
def diffuse():
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    tmp_graph=[[0]*r for _ in range(c)]
    for i in range(c):
        for j in range(r):
            if graph[i][j]==0 or graph[i][j]==-1:
                continue
            dust=graph[i][j]//5
            
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                
                if 0<=nx<=c and 0<=ny<=r and graph[nx][ny]!=-1:
                    tmp_graph[nx][ny]+=dust
                    tmp_graph[i][j]-=dust
    for i in range(c):
        for j in range(r):
            graph[i][j]+=tmp_graph[i][j]
    

def clean_air(start,dir): # 시작행 ,방향
    if dir==-1:
        for i in range(start-1,0,-1):
            graph[i][0]=graph[i-1][0] # up
        for j in range(0,r-1):
            graph[0][j]=graph[0][j+1] # right
        for i in range(0,start):
            graph[i][r-1]=graph[i+1][r-1] # down
        for j in range(r-1,1,-1):
            graph[start][j]=graph[start][j-1]
    else:
        for i in range(start+1,c-1):
            graph[i][0]=graph[i+1][0] # down
            
        for j in range(0,r-1):
            graph[c-1][j]=graph[c-1][j+1] # right
            
        for i in range(c-1,start,-1):
            graph[i][r-1]=graph[i-1][r-1] # up
            
        for j in range(r-1,1,-1):
            
            graph[start][j]=graph[start][j-1]
    
    graph[start][1]=0

cleaner=[]    
for i in range(c):
        for j in range(r):
            if graph[i][j]==-1:
                cleaner.append((i,j))
                
for i in range(t):
    tmp_graph=[[0]*r for _ in range(c)]
    
    visit=[[0]*r for _ in range(c)]               
    for i in range(c):
        for j in range(r):
            if graph[i][j]!=0 and graph[i][j]!=-1 and visit[i][j]==0:
                BFS(i,j)
        

    for i in range(c):
        for j in range(r):
            graph[i][j]+=tmp_graph[i][j]

                            
    clean_air(cleaner[0][0],-1)
    clean_air(cleaner[1][0],1)
    

sum=0

for i in range(c):
    for j in range(r):
        sum+=graph[i][j]


print(sum+2)



# 내 BFS 안됐던이유 -> tmp 를 t 돌릴때마다 초기화 해줘야되는데 계속 누적값이 쌓였음
# 또한 visit 배열 초기화 안해줘서 음수 발생 
# 아 ㅈㄴ 어렵다 씌발
            
            
'''
3 3 1
0 30 7
-1 10 0
-1 0 20

3 3 1
5 0 0
0 0 0
0 0 0

'''
