N,M=map(int,input().split())

graph=[[0]*N for _ in range(N)]

for i in range(N):
    graph[i]=list(map(int,input().split()))

cloud=[(N-1,0), (N-1,1), (N-2,0), (N-2,1)]


di,dj=[0,0,-1,-1,-1,0,1,1,1],[0,-1,-1,0,1,1,1,0,-1]
dx=[-1,-1,1,1]
dy=[-1,1,-1,1]

for i in range(M):
    D,S=map(int,input().split())
    cloud_new=[] 
    # 구름이동 + 물증가 
    for ci,cj in cloud:
        ni=(ci+di[D]*S+N)%N # direction 을 step 만큼 반복 , 연결돼있는 이동 -> (~+N)%N 연산 이용
        nj=(cj+dj[D]*S+N)%N
        
        graph[ni][nj]+=1
        cloud_new.append((ni,nj)) # 이동된 구름 리스트 (없어질거)
        
    # 이동한 구름 대각선 4방향 검사
    for ci,cj in cloud_new: # 새로운 현재 좌표 꺼내옴
        for i in range(4): # 대각선 4방향 좌표
            ni=ci+dx[i]
            nj=cj+dy[i]
            
            if 0<=ni<N and 0<=nj<N and graph[ni][nj]>=1: # 유효한 범위 이면서 물이 존재하는만큼
                graph[ci][cj]+=1 # 현재 좌표 물 증가
    
    cloud=[] # 새로 담기 위해 초기화
    # 전체 순회 하며 cloud_new 가 아니면서 2 이상인 grpah 요소들을 2빼고 cloud 로 새로변경
    for i in range(N):
        for j in range(N):
            if graph[i][j]>=2 and (i,j) not in cloud_new:
                graph[i][j]-=2
                cloud.append((i,j))
sum=0      
for i in range(N):
    for j in range(N):
        sum+=graph[i][j]

print(sum)

# 21610 / Simulation
# 처음에 붙어있는 배열에서의 이동을 조건문으로 일일히 처리 하려고 했음
# 수식 이용하면 간단하게 구현 가능 
# 대각선이동이 포함된 8 방향 이동은 다음과 같이 구현
# di,dj=[0,0,-1,-1,-1,0,1,1,1],[0,-1,-1,0,1,1,1,0,-1] 이동 가능한 좌표들을 적어둔후 
# direction ex) 1 이면 왼쪽 y 좌표 인 di 는 0 x 좌표인 dj 는 -1 
# 이걸 step 만큼 반복하면 된다
# 이걸 이용해서 구름이 이동한 지점의 좌표의 물을 1씩 늘리고 이동된 구름의 좌표를 저장해 둔다.
# 이동된 구름 기준으로 대각선을 검사하면서 해당 대각선 좌표가 유효범위 내이면서 물이 존재한다면
# 해당 구름좌표의 물을 1 증가시킨다.
# 위작업이 모두 끝나면 현재 이동된 구름이 아니면서 물의 좌표가 2 이상인 좌표들을
# 초기화한 새로운 구름 리스트에 담아둔다
# 리스트 보다 튜플이 더 빠르다
