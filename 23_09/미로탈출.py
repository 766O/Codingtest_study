'''
이것이 코딩테스트다 - ch05 / DFS,BFS

동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이 를 피해 탈출해야 한다.
동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있 다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 
이때 동빈이가 탈출하기 위해 움직여야 하는 최 소간의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

입력조건 
 첫째 줄에 두 정수 N. M(4 S N. M S 200)이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수(0혹은 1)로 미로의 정보가 주어진다. 각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸 과 마지막 칸은 항상 1이다.

입력예시
5 6
101010
111111
000001
111111
111111

출력예시 
10
'''

from collections import deque

N,M=map(int,input().split())

maze = [0 for _ in range(N)] 

for i in range(N):    
	maze[i] = list(map(int, input()))
 
maze_cnt=[0 for _ in range(N)]
for i in range(N):
    maze_cnt[i]=[0] *M
    
maze_cnt[0][0]=1



que=deque()

que.appendleft([0,0])


dx=[0,0,1,-1]
dy=[1,-1,0,0]

cnt=0

while que:

    x,y=que.popleft()
    maze[y][x]=0
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if nx<0 or nx>=M or ny<0 or ny>=N:
            continue
        if maze[ny][nx]!=1:
            continue
        
        que.append([nx,ny])
        maze_cnt[ny][nx]=maze_cnt[y][x]+1
        


#print(maze)
#print(maze_cnt)

print(maze_cnt[N-1][M-1])

# BFS
# 전형적인 BFS 문제 , 이전에 풀었던 풀이들을 기억하면서 조건코드를 노트에 필기후 코드 작성함 
# 나름 시행착오 없이 성공 , 하지만 입력 받는 부분 연습 필요 아직도 자동으로 안나옴 
# 또한 카운트 세는 2차원 리스트를 하나 더 선언했는데 정석 풀이에서는 미로로 입력받은 2차원 리스트 이용해서
# 1개의 2차원리스트로만 작성돼있었음 
    






    







        
