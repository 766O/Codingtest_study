from collections import deque

c,r=map(int,input().split())

graph=[[0]*r for _ in range(c)]


for i in range(c):
    graph[i]=list(input())

def BFS(i,j):
    #import pdb;pdb.set_trace()
    visit=[[0]*r for _ in range(c)]
    que=deque()
    que.append((i,j))
    visit[i][j]=-1

    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    while que:
        x,y=que.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>=c or ny<0 or ny>=r:
                continue
            if visit[nx][ny]==0 and graph[nx][ny]=='L':
                que.append((nx,ny))
                visit[nx][ny]=visit[x][y]+1
    
    
    max=-999
    #print(visit)
    
    for i in range(c):
        for j in range(r):
            if visit[i][j]>max:
                max=visit[i][j]
                
    return max
            
    
    
#print(BFS(0,6))

max=0
distance=0    
for i in range(c):
    for j in range(r):
        if graph[i][j]=='L':
            distance=BFS(i,j)
            
            if distance>max:
                max=distance
print(max+1)

# 2589 / BFS,Graph
# 풀이설계~코딩 + 반례 생각해서 수정까지 완벽하게 함
# 무난한 상하좌우 탐색 문제 
# 모든 좌표에 대해서 BFS 수행해서 각 좌표의 최장경로 값을 return 받은뒤
# 모든 좌표에 대해 반복문 돌면서 만약 해당 좌표의 최장경로 값이 max 경신할경우
# max 값 업데이트
# 처음 제출했을때 아래와 같이 길이가 1인 케이스 통과 못했음 
# 2 2
# LL
# WW 
# visit 배열에 경로 길이 저장하다보니 출발점은 항상 0 이었음 
# 0 이니까 BFS 끝나고 다시 출발점을 방문하며 의도 한것 보다 1번씩 더 방문했음
# 이를 방지하기 위해서 초기값 넣을때 출발 좌표에 -1 을 넣어 놓고
# 최종 값 뽑을 때 1씩 더해주어서 처리
