'''
import sys
sys.setrecursionlimit(10**7)

N=int(input())

matrix=[[0]*(N+1) for _ in range (N+1)]


for i in range(N-1):
    n,m=map(int,(input().split()))
    
    matrix[n][m]=1
    matrix[m][n]=1


visit=[0 for _ in range (N+1)]
parent=[0 for _ in range (N+1)]



def DFS(n):
 
    
    #print(n,end=" ")
    
    visit[n]=1
    
    for i  in range (len(matrix[n])):
        if visit[i]==0 and matrix[i][n]==1:
            parent[i]=n
            DFS(i)
            
DFS(1)


for i in range(2,N+1):
    print(parent[i])
'''
# 기존 DFS,BFS 관련 문제풀이시 항상 접근하던 인접행렬방식으로 DFS 이용함
# 이 문제의 경우 최대 입력이 100000 이므로 2차원 배열인 인접행렬 구성시 메모리 초과가 발생
# 문제풀이 접근방법은 맞았음
# 임의 정점에서 DFS 시작 -> 모든 정점을 탐방하게 된다
# 현재 들린 정점에서 조건을 만족하는 다음 정점으로 이동하기전에 parent라는 배열에 현재 정점에 해당하는 값을 다음 정점값에 해당하는 인덱스에 넣어놓음
# ex) 1 이 4 와 6 과 연결돼있는경우 4방문 이전에 parent[ x 0 0 0 1 0 0 0 ] 이런식으로 변경되고 4는 2 와 7과 연결 돼있으므로 
# 4가 2에 방문하기 전에 parent[x 0 0 4 1 0 0 0] 이런식으로 부모관계를 배열에 저장해놓는다
import sys
sys.setrecursionlimit(10**7)

N=int(input())

matrix=[[] for _ in range (N+1)]


for i in range(N-1):
    n,m=map(int,(input().split()))
    
    matrix[n].append(m)
    matrix[m].append(n)


visit=[0 for _ in range (N+1)]
parent=[0 for _ in range (N+1)]



def DFS(n):
 
    
    #print(n,end=" ")
    
    visit[n]=1
    
    for i  in matrix[n]:
        if visit[i]==0 and i in matrix[n]:
            parent[i]=n
            DFS(i)
            
DFS(1)


for i in range(2,N+1):
    print(parent[i])

# 해당 문제 조건에 맞게 인접행렬이 아닌 그래프의 연결상태만 표현해줌
# 그 이외 방법은 동일

