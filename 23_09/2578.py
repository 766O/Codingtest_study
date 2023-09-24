board=[[0]*5 for _ in range(5)]

for i in range(5):
    board[i]=list(map(int,input().split()))

read=[[0]*5 for _ in range(5)]

for i in range(5):
    read[i]=list(map(int,input().split()))
    
i=0
jx=0
cnt=0

    
row_bingo=[99,99,99,99,99]



def find_bingo(board,idx):
    cnt=0
    
    
    for i in range(5):
            if board[i]==row_bingo:
                #print('row_bingo')
                cnt+=1
                
                
    for i in range(5):
        if [board[j][i] for j in range(5)] == row_bingo:
            #print('col_bingo')
            cnt+=1
    tmp=0
    for i in range(5):
        for j in range(5):
            if i+j==4:
                tmp+=board[i][j]
    
    if(tmp==99*5):
        #print('diag_bingo')
        cnt+=1
        
    tmp=0
    for i in range(5):
        for j in range(5):
            if i==j:
                tmp+=board[i][j]
    
    if(tmp==99*5):
        #print('diag_bingo')
        cnt+=1
    return cnt
                
        
cnt_read=0

while(1):

    if(jx==5):
        i+=1
        jx=0
        
    if(i==5):
        break
    find=read[i][jx]
    
    for i_ in range(5):
        for j_ in range(5):
            if board[i_][j_]==find:
                board[i_][j_]=99
    
    res=find_bingo(board,i)
    if res>=3:
        break
    jx+=1
    cnt_read+=1
    

print(cnt_read+1)

# 2578 / implementation
# 처음부터 끝까지 풀기 성공
# 2차원 리스트 다루는법 숙지하기 
# 2차원 리스트중 열만 꺼내오고 싶으면 다음과 같이 작성 -> 하나씩 꺼내와서 리스트로 만든다
for i in range(5):
    [board[j][i] for j in range (5)]

# 5*5 인덱스 범위 내에서 사회자가 읽어준 자리에 해당하는 빙고판을 99로 바꿔 놓고 
# 매번 빙고가 발생했는지 검사
# 가로 세로 빙고는 [ 99 99 99 99 99 ] 배열을 만들어 동일하면 cnt+1 
# 대각선 빙고는 좌,우 총 2개 존재 각각 인덱스 특징을 이용하해서 대각선 모든 값의 합이 
# 99*5 즉 모두 방문했다면 cnt+1d
# 마지막으로 검사를 끝내고 나왔을때 동시에 빙고가 2개에서 4개로 되는 경우도 존재하므로
# 빙고 카운트가 3개이상이 되는 시점에서 종료하고 그때까지 사회자가 읽은 번호 개수 반환
# 간단한 구현문제지만 아직 어렵당 ^^; 1:20 소요    
