from collections import deque

w,h=map(int,input().split())

# 주어진 지도의 외곽에 1줄씩 추가 (상,하,좌,우)
graph=[[0]*(w+2) for _ in range(h+2)]

# (1,1) ~ (8,4) 채워 넣기
for i in range(1,h+1):
    graph[i][1:w+1]=(map(int,input().split()))

# 육각형 이동 가능 좌표 -> 짝수줄 홀수줄 에 따라 다르다 
dy=[0,1,1,0,-1,-1]
dx=[[1,0,-1,-1,-1,0] , [1,1,0,-1,0,1]]



def BFS(y,x):
    que=deque()
    que.append((y,x))

    visit=[[0]*(w+2) for _ in range(h+2)]
    visit[y][x]=1
    cnt=0
    
    while(que):
        y,x=que.popleft()
        
        
        for i in range(6):

            nx=x+dx[y % 2][i] # 짝수면 [1,0,-1,-1,-1,0] 홀수면 [1,1,0,-1,0,1]
            ny=y+dy[i]
        
            # 핵심은 회색건물('1')을 탐색하는 것이 아닌 주변 흰색 부분('0')을 탐색한다는 점이다. 
            # 이렇게 풀이하면 회색 건물('1)에 둘러싸인 흰색 부분('0')을 탐색하지 않기 때문에 
            # 초기 접근 방식에서 해결하지 못한 점을 해결할 수 있다.
            if 0<=ny<h+2 and 0<=nx<w+2:
                if graph[ny][nx]==0 and visit[ny][nx]==0:
                    visit[ny][nx]=1
                    que.append((ny,nx))
                elif graph[ny][nx]==1:
                    cnt+=1
                
                
    return(cnt)

print(BFS(0,0))

# 5547 / Graph,BFS
# 육각형 좌표에서 이동범위는 짝수줄,홀수줄에 따라 다으다
# 문제풀이의 핵심 외곽에 추가로 0 인 육각형들을 만들어주고 
# 0,0 부터 정육각형 이동범위로 탐색 , 회색 건물(1) 을 만나면 cnt를 늘림 
# ex) 0,0 은 이동범위로 이동하면서 회색 건물(1) 을 1번 만나고
# 1,1 에서는 이동범위로 움직이면서 회색건물(1) 을 2번 만난다
# 링크 그림 참조 - https://reliablecho-programming.tistory.com/110
# 이 방식을 이용해야 회색건물(1) 에 둘러싸인 흰색건물(0) 은 카운트 하지 않는다 

# 처음 에는 늘 하던대로 조건 줬는데 
#if nx<0 and nx>=h+2  and ny<0 and ny>=w+2:
#                continue 
#
# continue 와 조건맞을때만 들어가는거의 조건문 차이? 
# 아마 이 문제는 0,0 부터 시작해서 전 좌표를 이동해가면서 확인
# 저거 쓰던문제는 조건에맞는 1 인경우만 큐에넣고 했을거임 

