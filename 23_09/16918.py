from collections import deque

R,C,N=map(int,input().split())
check=[[0]*C for _ in range(R)]

for i in range(R):
    check[i]=list((input()))

sec=0

dx=[1,0,-1,0]
dy=[0,1,0,-1]

visit=[[0]*C for _ in range(R)]
que=deque()

def BFS(que,check):

    while que:
        x,y=que.popleft()
        check[x][y]='.'
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx>=0 and nx<R and ny>=0 and ny<C:
                
                if check[nx][ny]=='O':
                    check[nx][ny]='.'
                    
def simulate(time):
    global check,que
    
    if time==1:
        for i in range(R):
            for j in range(C):
                if check[i][j]=='O':
                    que.append((i,j))
    elif time %2==1:
        BFS(que,check)
        for x in range(R):
            for y in range(C):
                if check[x][y]=='O':
                    que.append((x,y))
    else:
        check = [['O']*C for _ in range(R)]

for i in range(1,N+1):
    simulate(i)

for row in check:
    print(''.join(row))        

# 16918 / BFS 
# 문제이해를 전혀하지 못함 
# 남의 풀이보고 이해했음 
# 폭탄 터뜨리는 (순회하는 )역할인 BFS 와 시간에따라 시뮬레이션하는 simulate 두가지로 나눠서 구성
# BFS 내에서 한꺼번에 처리할 필요 없음 


# 1초 -> 폭탄이 존재하는 위치를 넣어줌
# 2초 -> 모든위치에 폭탄 설치
# 3초 -> 1초일때 넣어둔 큐의 좌표의 폭탄이 터짐 
# BFS는 우선 폭탄이 존재하는 위치를 알려주는 인덱스를 큐에서 뽑아오고 그 위치를 .으로 변경
# 3초일때 check는 모두 폭탄이 존재 , 큐에서 뽑아온 인덱스의 상하 좌우는 모두 폭탄이므로 .으로 변경
# 하면 폭발한 결과가 나오게 됨 
# BFS 이후 남은 폭탄들을 큐에 다시 저장해두고 
# 4초 -> 다시 모든위치에 폭탄 설치
# 5초 -> 똑같이 BFS 반복 , 큐에서 좌표 받아와서 해당하는 상하좌우 터뜨리기 (모든 check 는 폭탄이다)
# 반복                          

    
    


        
