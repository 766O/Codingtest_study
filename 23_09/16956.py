from collections import deque

r,c=map(int,input().split())

map=[[0]*c for _ in range(r)]

for i in range(r):
    map[i]=list(input())

que=deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def BFS(que):
    while que:
        x,y=que.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #import pdb;pdb.set_trace()
            if nx>=0 and nx<r and ny>=0 and ny<c and map[nx][ny]=='.':
                map[nx][ny]='D'
                
def find_sheep(que):
    while que:
        x,y=que.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
        
            if nx>=0 and nx<r and ny>=0 and ny<c and map[nx][ny]=='S':
                return 0
    return 1
                
                

for i in range(r):
    for j in range(c):
        if map[i][j]=='S':
            que.append((i,j))

BFS(que)
que2=deque()

for i in range(r):
    for j in range(c):
        if map[i][j]=='W':
            que2.append((i,j))
            
res=find_sheep(que2)

print(res)

if(res==1):
    for i in map:
        print(''.join(i))

# 16956 / BFS
# 문제에는 안쓰여있지만 출력되는 목장 상태는 예시와 달라도 됨
# 우선 양에 해당하는 S를 만나면 해당 인덱스를 que1 에 넣어놓고
# 모든 양을 돌면서 모든양의 위치 상하 좌우에 D 울타리를 설치함 
# 그후 늑대에 해당하는 W를 만나면 해당인덱스를 que2 에 넣어놓고
# 모든 늑대를 돌면서 S 와 만날 수 있는지 검사 
# 만약 만나는 경우 0 을 return 하고 모든 늑대에대해서 양과 만나지못하면 1을 return 
# reutrn 값에 따라 목장상태 출력
