from collections import deque

N=int(input())

adj=[0]+[int(input()) for _ in range(N)]
result=[]


# v 현재 좌표 / i 시작좌표
def dfs(v,i):
    visited[v]=1 # 현재좌표 방문처리
    w=adj[v] # 현재좌표와 연결되있는 값 받아와서 
    if visited[w]==0: # 연결되있고 방문안했으면 
        dfs(w,i) # dfs
    elif visited[w] and w==i: # 방문을 이미 했거나(싸이클) 싸이클이라면
        result.append(w)

for i in range(1,N+1):
    visited=[0]*(N+1)
    dfs(i,i)

print(len(result))
result.sort()

for i in result:
    print(i)

# 2668 / DFS 
# 싸이클을 찾는 문제였음 
# 싸이클에 해당하는 노드들을 모두 찾아주고 결과에 저장해놓으면됨
# DFS를 통해 싸이클을 찾는다
# 해당 코드에서는 그냥 두번째 숫자들을 하나의 리스트 에 저장한뒤
# 첫번째 숫자줄을 반복문 통해 모두 확인해봄 
# ex) dfs(1,1) 로 시작하면 visited[1] = 1 1번숫자 방문처리한 후 adj[1] 즉 첫번째숫자 1번 아래 있는
# 값(3)을 w 에 담아줌 이 w 가 만약 방문이 안돼있다면 dfs(3,1) 을 진행 
# dfs(3,1)을 실행하면 3 아래에 있느 값을 w 에저장 (1) 이때 (1)이라는 숫자는 이미 방문했던 좌표이므로 
# 싸이클에 해당 result 배열에 1을 추가 해놓음 
# 이 과정을 첫번재 숫자줄에대해 모두 반복하면 싸이클에 해당하는 모든 노드를 구할 수 있다
