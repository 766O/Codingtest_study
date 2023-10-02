from collections import deque

m,n,h=map(int,input().split())

tomato=[[[0 for _ in range(m) ] for _ in range(n)] for _ in range (h)]

for i in range(h):
    for j in range(n):
        tomato[i][j]=list(map(int,input().split()))
        
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dh=[0,0,0,0,-1,1]

#print(tomato)

def BFS(que):
    while que:
        
        height,x,y=que.popleft()
    
        global max_h
        global max_x
        global max_y
    
        max_h=height
        max_x=x
        max_y=y
    
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nh=height+dh[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m or nh<0 or nh>=h:
                continue
            
            if tomato[nh][nx][ny]!=0 or tomato[nh][nx][ny]== -1 or tomato[nh][nx][ny]==1:
                continue
            
            if tomato[nh][nx][ny]==0: 
                que.append([nh,nx,ny])
                tomato[nh][nx][ny]=tomato[height][x][y]+1
                
                max_h=nh
                max_x=nx
                max_y=ny
                
que=deque()

for i in range (h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==1:
                que.append([i,j,k])
                
BFS(que)


for i in range (h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==0:
                print(-1)
                exit(0)
                




print(tomato[max_h][max_x][max_y]-1)      

# 7569 / BFS,Graph
# 7576 문제의 3차원 버젼
# 인덱스를 잘 생각하자 (해당 인덱스가 어디를 가리키고 있는지)
# 1에 대해서 너비우선 탐색을 진행 할것
# 즉, 해당 배열을 돌면서 1의 값을 가지고 있는 인덱스 위치들을 차례대로 큐에 넣고 진행하면 된다
# 따라서 내부의 BFS 함수는 그냥 큐에서 값 뽑아오면서 max_h,max_x,max_y를 갱신해주면됨 
# 그 후 총 움직일 수있는 6가지 경우에 대해 차례대로 탐색을 진행하면된다
# 이때 첫번째로 다음 인덱스가 유효한지 검사 
# 두번째로 인덱스가 유효할때 우리가 찾는 익지않은 토마토 (아직 탐색X) 인지 검사
# 마지막으로 익지않은 토마토(아직 탐색x) 라면 해당 인덱스를 큐에 새로 넣어주고 
# 해당위치에 몇일걸렸는지 기록 (이전 탐색인덱스의 값에 +1 )
# 마지막으로 max_h,max_x,max_y (마지막 방문 인덱스 ) 갱신
# 출력은 BFS를 진행헀음에도 0 이 남아있으면 방문 못하는 지점이 남아있다는 뜻
# 즉 못 익는 토마토가 존재하는 경우 이므로 -1 출력후 프로그램 종료
# 그 이외의 경우 몇일이 걸리는지 출력 , 이때 이미 익어있는(0) 인 경우도 포함됨 
