import sys
input = sys.stdin.readline
from collections import deque

N,M=map(int,input().split())

com=[ [] for _ in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    com[b].append(a)
    

visit=[0 for _ in range(N+1)]




def BFS(n):
    que=deque()
    que.append(n)
    
    cnt=0
    
    visit[n]=1
    
    while que:
        cur=que.popleft()
        
        for next in com[cur]:
            if visit[next]==0:
                que.append(next)
                visit[next]=1
                cnt+=1
    
    return cnt
            
result=[]     
for i in range(1,N+1):
    result.append((BFS(i)))
    visit=[0 for _ in range(N+1)]       

for i in range(len(result)):
    if max(result) == result[i]:
        print(i+1)

# 1325 / BFS
# 재귀 DFS로 풀면 왜 계속 메모리 초과?  
# DFS , BFS 차이점 적기  
# DFS -> 모든 노드를 방문하고자 할경우,속도는 BFS 비해서 느림
# BFS -> 주로 두 노드사이의 최단경로를 찾고 싶을떄
# 그래프의 모든 정점을 방문하는것이 주요한 문제 -> BFS / DFS 상관 X
# 경로의 특징을 저장해야 할때 , 모든경우를 전부 탐색하는 완전 탐색 / 순열,조합 구현 -> DFS
# 최단거리 구하는 문제 , 깊이 특징을 이용한 문제 -> BFS
# 100000 이상 입력받을때는 연결리스트로 만드는 방향으로
# 문제풀때 방향이 있는 그래프를 생각한것은 맞았음 
# 마지막 정답 제출양식 맞추기 
