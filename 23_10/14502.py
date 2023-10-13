from collections import deque
import itertools
import copy

n,m=map(int,input().split())

graph=[[0]*m for _ in range(n)]

for i in range(n):
    graph[i]=list(map(int,input().split()))
    

dx=[-1,1,0,0]
dy=[0,0,-1,1]

list_0=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            list_0.append((i,j))

comb=itertools.combinations(list_0,3)

comb=list(comb)

def BFS(x,y):
    que=deque()
    visit=[[0]*m for _ in range(n)]
    
    que.append((x,y))
    visit[x][y]=1
    
    while que:
        x,y=que.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<m and test_graph[nx][ny]==0 and visit[nx][ny]==0:
                que.append((nx,ny))
                visit[nx][ny]=1
                test_graph[nx][ny]=2

safe_list=[]
for i in range(len((comb))):
    test_graph = [[graph[i][j] for j in range(m)] for i in range(n)]
    
    test_graph[comb[i][0][0]][comb[i][0][1]]=1
    test_graph[comb[i][1][0]][comb[i][1][1]]=1
    test_graph[comb[i][2][0]][comb[i][2][1]]=1

    for i_1 in range(n):
        for j_1 in range(m):
            if test_graph[i_1][j_1]==2:
                BFS(i_1,j_1) 
    
    safe=0

    for i_2  in range(n):
        for j_2 in range(m):
            if  test_graph[i_2][j_2]==0:
                safe+=1

    
    safe_list.append(safe)
    
print(max(safe_list))

# 14502 / Graph,BFS
# 벽을 세우는것을 처리 못해서 힌트 보고 파이썬의 itertools 이용하면 조합,순열 구현가능
# 어차피 벽을세우는건 graph 내 0 의 위치를 3개 고르는것 과 동일함 
# 즉 graph 좌표에서 0 인 좌표들을 list0 에 추가하고 list0 에 대해 조합을 실행하면됨
# 그렇게 벽을 세울 수 있는 후보들을 정하면
# 후보들 개수만큼 반복하면서 test_graph 라는 변수에 graph 를 복사한후 
# 해당 후보 좌표에 벽을세움(1을 넣는다)
# 벽 세운후 BFS 시행 하고 
# 안전지대 개수 센다음에 safe_list 에 추가
# 모든 가능한 경우의수를 시행한다음에 그 중 최댓값 출력
# 3중 반복문이라 쫄았는데 돌아간다 -> 이제는 대략적으로 시간복잡도 계산할 줄 알아야 되지 않을까...
# 새로 얻어간것 itertools -> 조합,순열 구현되있는 라이브러리
