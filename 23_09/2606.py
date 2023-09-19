from collections import deque

N=int(input())
M=int(input())

connect=[]

for _ in range(N+1):
    connect.append([0]*(N+1))

for i in range(M):
    c1,c2=(map(int,input().split()))
    connect[c1][c2]=1
    connect[c2][c1]=1
    


visit=[0]*(N+1)

cnt=0

def BFS(num):
    que=deque()
    que.append(num)
    
    while que:
        num=que.popleft()
        global cnt
        
        if visit[num]==0:
            cnt+=1
            visit[num]=1
            for i in range(1,N+1):
                if connect[num][i]==1 and visit[i]==0:
                    que.append(i)
            
BFS(1)
print(cnt-1)

# 2606 / BFS 
# 처음부터 끝까지 아무 도움 없이 드디어 BFS 문제 해결
# 문제에서 원하는게 무엇인지 정확하게 파악해야함 
# 이 문제 같은경우 1에서 BFS 돌리면 1과 연결된 모든 정점 카운트 가능 
# 중간에 필요없는 break 문 작성해서 시간 까먹음 -> 어차피 조건에 안맞으면 방문 못하니까
# 그냥 큐 다 빌때 까지 루프 돌리면 알아서 끝남
# 구해야하는것? -> 1과 연결된 정점개수 !!!!!!
# 문제 자체는 간단, 틀렸습니다 떴을때 스스로 반례찾아서 디버깅하며 해결했다는데 의의를두자 
