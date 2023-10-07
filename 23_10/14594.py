from collections import deque

N=int(input())

M=int(input())

villain=[]
result=[]
flag=0

room=[0]*(N+1)


for i in range(M):
    x,y=map(int,input().split())
    villain.append([x,y])
'''   
처음접근법

now_min=999
now_max=-1

for i in range(len(villain)):
    new_x=villain[i][0]
    new_y=villain[i][1]
    
    if flag==0:
        flag=1
        result.append([new_x,new_y])
    else:
        for j in range(len(result)):
            old_x=result[j][0]
            old_y=result[j][1]
            
            if new_x<=old_x and new_y>=old_y:
                result[j][0]=new_x
                result[j][1]=new_y
            elif new_x<=old_x and new_y<=old_y:
                result[j][0]=new_x
            elif new_x>=old_x and new_y>=old_y and new_x<=old_y:
                result[j][1]=new_y
            else:
                result.append([new_x,new_y])


for i in range(len(result)):
    N=N-(result[i][1]-result[i][0])

if M==0:
    print(0)
    exit(0)

print(N)
'''     


for i in range(len(villain)):
    x,y=villain[i]
    
    for j in range(x,y):
            room[j]=1


cnt=0
for i in range(1,N+1):
    if room[i] == 0:
        cnt+=1
if M==0:
    print(N)
    exit(0)
    
print(cnt)


# 14594 / Simulation
# 처음 접근 -> 모든 입력쌍들을 받고 
# 숫자이어진 범위 저장할 result 리스트 생성
# 첫 입력쌍을 result 에 넣은뒤 모든 입력쌍을 보면서 조건에 맞게 이어지는 숫자 범위만 저장
# 그 후 이어진 범위만 남아있으므로 이를 이용해 출력 
# 시간초과 발생 

# 시간초과 발생해서 아예 다른 배열을 만들어서 기록해놓으려는 접근법 생각함
# 해당 범위만큼 벽이 무너지는걸 1로 표현 남아있는 방은 남아있는 벽을 세면 된다
# 주의 할점은 인덱스 잘생각하기 1-3 / 4-5 사이에 벽 1개는 존재해야한다 
# 이를 위해 범위 x,y 로 설정 
#  (1,3) , (2,4) , (5,8) 일경우 이어지는 범위는 1~4 / 5~8 임
# 맨 앞의 0은 인덱스 맞추기 위함
# [0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0]
