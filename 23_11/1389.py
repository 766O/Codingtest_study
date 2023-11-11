from collections import deque
import sys

N,M=map(int,input().split())

'''
graph=[[0]*(M+1) for _ in range(N+1)]

for i in range(M):
    A,B=map(int,input().split())
    graph[A][B]=B
    graph[B][A]=A
    
print(graph)
'''
'''
[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 3, 4, 0], 
[0, 0, 0, 3, 0, 0], 
[0, 1, 2, 0, 4, 0], 
[0, 1, 0, 3, 0, 5],
 [0, 0, 0, 0, 4, 0]]
 '''

graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

#print(graph)
# # [[], [3, 4], [3], [1, 4, 2], [1, 5, 3], [4]]

def BFS(i):
    que=deque()
    que.append(i)
    visit[i]=1
    
    while(que):
        ci=que.popleft()
        
        for i in graph[ci]:
            if not visit[i]:
                que.append(i)
                visit[i]=visit[ci]+1
    
            
        
        

result=[]
for i in range(1,N+1):
    
    visit=[0]*(N+1)
    BFS(i)
    result.append(sum(visit))
    
    
print(result.index(min(result)) + 1)

# 1389 / BFS
# 양방향 그래프를 이용 
# 인원의 수만큼 BFS 반복
# ex) 1 일경우 1은 1과 방문처리 해버림, 큐에 1을 넣는다 (시작)
# 큐에 들어있는 1을 꺼내서 for i in graph[ci] 로 1 과 연결된 3,4 검사
# 만약 3,4 가 아직 방문처리 안돼있다면 
# 큐에 3,4 넣어놓고 이전의 방문횟수 1보다 1증가한 2를 기록해놓는다
# 큐에는 3,4 가 남아있다
# 3에 대해서 for i in graph[ci] 로 3 과 연결된 1,4,2 검사
# 1과 4는 방문했기때문에 if 문 이후로 안넘어감
# 2 는 큐에 추가하고 이전 방문횟수 1보다 증가한 3을 기록
# ... 반복
# 인접리스트로 접근하는 방법이 더 편하다
# 항상 인접 행렬 말고 인접리스트도 생각하기
