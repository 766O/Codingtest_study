import sys

from collections import deque

N,M=map(int,input().split())

box=[]
for i in range(M):
    box.append(list(map(int,input().split())))
    
dx=[-1,1,0,0]
dy= [0,0,-1,1]


def BFS(que):
    

    while que:
        x,y=que.popleft()
        global max_x
        global max_y
        max_x=x # 1번만에 결과 나올경우 위해 초기화 해줘야함 
        max_y=y

        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or nx>=M or ny<0 or ny>=N:
                
                continue
            if box[nx][ny]==-1 or box[nx][ny]==1 or box[nx][ny]!=0:
                continue
            if box[nx][ny]==0:
                box[nx][ny]=box[x][y]+1
                
                max_x=nx
                max_y=ny
                
                que.append([nx,ny])

                
                
que=deque()

for i in range(M):
    for j in range(N):
        if(box[i][j]==1):  # 1이 여러개 있을경우를 위해서 1인경우 모두 큐에 넣고 시작해야함 
            que.append([i,j])
    
BFS(que)

#예외처리 -> BFS 로 모두 탐색해도 여전히 익지 않은 토마토 존재시 -1 출력
for i in range(M):
    for j in range(N):
        if (box[i][j]==0):
            print(-1)
            exit(0)      
#print(box)
print(box[max_x][max_y]-1)


# 7576 / BFS
# 처음에 겁나 어려웠던 문제 전체적인 흐름은 기본BFS 와 동일하나 여러 조건때문에 까다롭게 느껴짐
# 만약 2차원리스트의 범위 안이면서 , 우리가 관찰하고자하는 안익은 토마토 (0) 인경우 , 
# (-1 -> 못간다 / 1-> 시작시 익어있던 토마토 / 그이외 0이 아닌수 ->이미 방문해서 몇일후에 익었는지 기록된것) 에 대해서만 탐색 진행
# 탐색한 토마토는 익게 되는데 이때 기존 2차원리스트에 몇일만에 익었는지 day 값을 넣어줌 
# 또한 마지막에 방문한 토마토가 가장 오랜시간 지난후 익은 토마토니까 해당 인덱스를 max_x,max_y 값으로 따로 보관하다가
# BFS 종료 후에 해당 인덱스의 값을 통해 print 하면 가장 최대 날짜가 출력됨 
