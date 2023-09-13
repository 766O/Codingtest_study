''' 
import sys

input=sys.stdin.readline

def make_matrix(n_list):
    matrix=[[0]*(len(n_list)+1) for i in range(len(n_list)+1)]
    for i in range(1,len(n_list)):
        matrix[i][n_list[i]]=1
        matrix[n_list[i]][i]=1
    
    return matrix

def DFS(root,graph,visited):
    visited[root]=1
    #print("visit:",root,end=" ")
    
    for i in range(len(graph[root])):
        if graph[root][i]==1 and visited[i]==0:
            DFS(i,graph,visited)

# 입력 함수
T=int(input())
n_list=[[] for i in range(T)]
visited=[[] for i in range(T)]
matrix=[[] for i in range(T)]

    
for i in range(T):
    #import pdb;pdb.set_trace()

    N=int(input())
    n_list[i]=list(map(int,input().split()))
    visited[i]=[0]*(N+1)
    n_list[i].insert(0,0)
    
    matrix[i]=make_matrix(n_list[i])

    

for i in range(T):
    cnt =0
    start=1
    for j in  range(len(visited[i])):
        cnt+=1
        
        DFS(start,matrix[i],visited[i])
        
        for j in range(len(visited[i])):
            if visited[i][j]==0:
                start=j

    print(cnt)
'''

# 이전에 풀었던 문제처럼 인접행렬로 풀려고했는데 메모리 초과 발생 -? 왜???

import sys
sys.setrecursionlimit(10**7)

T=int(input())

def DFS(V):
    visit[V]=1
    next=arr[V]
    
    if visit[next]==0:
        DFS(next)

for i in range(T):
    cnt=0
    
    N=int(input())
    arr=[0]+list(map(int,input().split()))
    visit=[0]*(N+1)
    
    for i in range(1,N+1):
        if visit[i]==0:
            DFS(i)
            cnt+=1
    print(cnt)
    
    
# 10451 / Graph
# 싸이클의 수가 총 DFS 반복 횟수인것은 알아챘지만 내 방식은 메모리 초과 발생
# 그래프 표현시 무조건 인접행렬로 할 필요는 없음 1차원 배열 을 통해 표현할수 있음
# 문제를 읽고 생각을하자 !!!
# 해당 문제에서 핵심은  1차원 배열의 인덱스를 기준으로 정점 방문 여부를 판단한후에 
# 다음 방문 정점은 해당배열의 인덱스가 가리키는 값임 즉 visit[v]=1 로 방문한다음에 다음 방문 정점은 next=arr[v] 라고 
# 표현 하는 것 

# 입출력 다양한 문제를 풀면서 익숙해져야 할 듯 싶다... 
# 입력받은 문자열을 정수형 리스트로 만들고 싶으면 list(map(int,input().split()))
