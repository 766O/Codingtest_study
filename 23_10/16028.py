from collections import deque
import copy

N,M=map(int,input().split())

visit=[0]*101
ladder_snake=[0]*101


for i in range(N+M):
    u,v=map(int,input().split())
    ladder_snake[u]=v

que=deque()
que.append(1)
visit[1]=1

nx=[]

while que:
    #import pdb;pdb.set_trace()
    x=que.popleft()
    
    if(x+1<=100):
        nx.append(x+1)
    if(x+2<=100):
        nx.append(x+2)
    if(x+3<=100):
        nx.append(x+3)
    if(x+4<=100):
        nx.append(x+4)
    if(x+5<=100):
        nx.append(x+5)
    if(x+6<=100):
        nx.append(x+6)
    
    for nnx in nx:
        if ladder_snake[nnx]!=0:
            nnx=ladder_snake[nnx]
        if nnx==100:
            print(visit[x])
            exit(0)
        elif nnx<100 and visit[nnx]==0:
            visit[nnx]=visit[x]+1
            que.append(nnx)

        
# 16028 / BFS
# 핵심은 사다리와 뱀을 어떻게 구현하는가였음
# ladder_snake[u]=v 배열을 통해 구현 
# 만약 사다리나 뱀이 위치한 곳에 있다면 해당 배열의 값으로 바꿔주면 된다 (LUT 처럼)

# 주사위로 이동 가능한 경우의 수를 nx 에 모두 넣은다음에 
# 주사위로 이동한경우 모두를 보면서사다리나 뱀 으로 이동가능한경우 (if ladder_snake[nnx]!=0)   
# 이동후 위치가 100이라면 몇번 걸렸는지 출력후 종료
# 만약 아직 100에 도착하지 못했다면 que 에 넣고 방문처리    
    
