import sys
from collections import deque # que 위한 라이브러리 

N,M,V=map(int,input().split())

matrix=[[0] * (N+1) for _ in range(N+1)]  # N+1 개의 요소를 가지는 빈 리스트를 N+1 개 만큼 만듬
bfs_visited = [0] * (N+1)
dfs_visited=[0] * (N+1)

for i in range(M): # 인접 행렬 만들기
    n1,n2=map(int,input().split())
    matrix[n1][n2]=1
    matrix[n2][n1]=1


BFS_list=[]
DFS_list=[]

#BFS 는 큐이용
def BFS(root,graph,visited):
    
    queue=deque([root]) # 첫번째 정점을 큐에 넣어놓고 
    bfs_visited[root]=1 # 첫번째 정점 방문처리 
    
    while queue: # 만약 큐가 비어있지 않다면 
        v=queue.popleft() # 해당 정점을 팝 하면서 방문했다고 출력
        BFS_list.append(v)
        print(v,end=' ')

        for i in range(len(graph[v])): # 해당 정점과 인접한 정점들을 돌면서 
            if bfs_visited[i]!=1 and graph[v][i]==1: # 인접하면서 아직 방문하지 않았다먄
                queue.append(i) # 큐에 해당 정점을 추가 해주면서
                bfs_visited[i]=1 # 방문했다고 처리 
                
                
#DFS 는 스택 이용
def DFS(root,graph,visited):
    dfs_visited[root]=1 # 첫번째 정점을 방문했다고 처리 
    DFS_list.append(root)
    print(root,end=' ') # 방문했다고 출력
    
    for i in range(len(graph[root])): # 해당 정점과 인접 정점들을 돌면서
        if graph[root][i]==1 and dfs_visited[i]!=1: # 정점과 인접하면서 방문하지 않았다면
            DFS(i,graph,visited) # 해당정점에 대해서 DFS 재귀적으로 적용 (더 이상 방문 못할때까지 작동함)


DFS(V,matrix,dfs_visited)
print()
BFS(V,matrix,bfs_visited)


#1260 / DFS,BFS
