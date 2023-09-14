import sys
from collections import deque # que 위한 라이브러리 
input = sys.stdin.readline

def next_num(num,pow): # 입력받은 문자 숫자의 다음 숫자를 만듬 
    num_list=list(map(int,num)) #리스트 에 들어있는 요소들을 정수로 변환한 후 차례로 리스트에 넣어놓는다.
    num=0
    
    for i in range(len(num_list)): # 해당 리스트의 길이만큼 반복하면서 
        num=num+int(num_list[i])**pow # 들어있는 요소값을 문제의 조건처럼 제곱해주고 더해서 새로운 다음 숫자를 만듬
    
    return num # 정수형태로 반환
    


def DFS(V,count,pow):
    if(visited[int(V)] != 0): # 만약 이전에 방문했던 곳, 즉 이전에 나온 숫자면 싸이클이 생기는거임 
        return visited[int(V)] -1  # 이 경우에 첫번째에 나올때 까지 걸린 count 가 해당 숫자 인덱스 가 나타내는 배열에 저장 돼있음 1 빼고 반환

    visited[int(V)]=count # 방문하면서 해당 숫자의 인덱스가 나타내는 배열에 몇번째로 나온수인지 count
    
    num=next_num(V,pow) # 다음숫자 제작
        
    count+=1 # 카운트 1늘림

    
    return DFS(str(num),count,pow) # return 이 있고 없고의 차이 ?

        
A,P=input().split()


visited=[0]*236197 # 최대 가능 길이

cnt=1

re=DFS(A,1,int(P))

print(re)

# 2331 / Graph
# "언젠가 이와 같은 반복수열이 된다" 이 문장에 포인트가 있다고 생각합니다. DFS나 BFS는 visited가 되어있으면 탐색을 종료,
# 이렇게 언제 끝날지 모르는 탐색문제는 BFS나 DFS가 보통 정해

# 무작정 DFS/BFS 문제라고 냅다 만들지말고 DFS/BFS 를 어떻게 이용할건지가 중요 -> 위에 적었듯이 언제 끝날지 모를때,즉 다시 방문할때 멈춰야할때 가 포인트

'''
int f() {
  if (베이스 조건) {
  	return 베이스
  }
  else { // 베이스 조건이 아닐때,
    [재귀식 연산에 대한 고려]
    return 재귀식;
  }
}
'''

# 재귀함수 통해 뭔가 값을 반환 받으려면return 필요 , 단순 print 는 필요 x 
