n=int(input())

def change(switch,n): # 인덱스 기준 바꿈
    if switch[n]==0:
        switch[n]=1
    else:
        switch[n]=0

def wide(switch,number):
    n_idx=1
    change(switch,number-1)

    if number-1-n_idx<0 or number-1+n_idx>=n:
        return
    
    while switch[number-1-n_idx]==switch[number-1+n_idx] and number-1-n_idx>=0 and number-1+n_idx<n:
        
        change(switch,number-1-n_idx)
        change(switch,number-1+n_idx)
        n_idx+=1
        if number-1-n_idx<0 or number-1+n_idx>=n:
            return

    

switch=[]

switch=list(map(int,input().split()))

student=int(input())    

for j in range(student):
    sex,number=map(int,input().split())
    if sex==1:
        for i in range(n):
            if (i+1)%number==0:
                change(switch,i)
    else:
        wide(switch,number)


for i in range(n):
    print(switch[i],end=" ")
    if i%20==19:
        print()
        
# 1244 / Implementation

# 출력형식 맞추느라 오래걸림...
# 남자에 해당하는 switch 함수로 해당 번호에 해당하는 값을 변경시킴
# 여자의 경우 기준으로 주어진 number 값을 바꾼 이후 양족이 대칭인지 지속적으로 확인해나가야함
# 이 과정을 while 함수로 구현 했는데 Index error 가 계속 발색했음 (길이가 1 또는 2인 경우 등)
# 좌우 확인후 change 한 다음에 늘어난 인덱스가 유효한지 확인해줘야함
# 이 부분을 n_idx 증가시킨이후 유효한지 확인을 통해서 만약 유효하다면 지속하고 아닌경우 종료 
     


    
