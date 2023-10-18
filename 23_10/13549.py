from collections import deque

n,k=map(int,input().split())

time=[0]*(100001)
visit=[0]*(100001)


que = deque()
que.append(n)



    
while que:
        x=que.popleft()
        visit[x]=1
        
        if x==k:
            print(time[k])
            break
        
        nx1=x+1
        nx2=x-1
        nx3=x*2
            
        if nx3>=0 and nx3<100001 and visit[nx3]==0:
            time[nx3]=time[x]
            visit[nx3]=1
            que.appendleft(nx3) # 가장 먼저 확인 해봐야함 넣을떄 큐의 가장 앞쪽으로 들어감 
        
        if nx2>=0 and nx2<100001 and visit[nx2]==0:
            time[nx2]=time[x]+1
            visit[nx2]=1
            que.append(nx2)
            
        if nx1>=0 and nx1<100001 and visit[nx1]==0:
            time[nx1]=time[x]+1
            visit[nx1]=1
            que.append(nx1)

# 13549 / BFS
# 큐에서 pop를 한 값에 따라 x * 2, x - 1, x + 1을 각 조건에 확인해서 큐에 추가       
# 가장핵심 -> 큐에 추가할때 순간이동 하는 x * 2 를 먼저 넣어줘야함 

# ex) N과 K 값이 3, 5
# 탐색을 X - 1, X + 1, X * 2 순으로 bfs 하면
# 2 4 6                             +1
# 1 (3) (4) / (3) 5 8 / (5) 7 12    +1
# 총 2초 소요 

# 탐색을 X * 2, X - 1, X + 1 순으로 하면
# 6 2 4                             +0 (순간이동)
# 12 5 7 / 8 (3) (5) / (4) 1 (3)    +1
# 총 1초 소요 

# BFS 인데 왜 visited 안만들어서 중복으로 탐색하게 만들었을까? ... 빡대가린가 보다
