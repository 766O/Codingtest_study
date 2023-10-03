key=[['q','w','e','r','t','y','u','i','o','p'],
['a','s','d','f','g','h','j','k','l','_'],
['z','x','c','v','b','n','m','_','_','_']]

def distance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def is_left_right(key):
    if key=='q'or key=='w'or key=='e'or key=='r' or key=='t'or key=='a'or key=='s'or key=='d'or key=='f'or key=='g'or key=='z'or key=='x'or key=='c'or key=='v':
        return 1 #왼손
    else:
        return 0 #오른손

def is_diff(key1,key2):
    if is_left_right(key1)==is_left_right(key2):
        return 0 # 동시에 누를 수 없음
    else:
        return 1 # 동시에 누를 수 있음

def find_idx(ch):
    for i in range(3):
        for j in  range(10):
            if key[i][j]==ch:
                return([i,j])
            

l,r=input().split()            
str=input()

idx=0
time=0
flag=0

left=find_idx(l)
right=find_idx(r)

n_left=[0,0]
n_right=[0,0]



for i in range(len(list(str))):
    char=str[i]
    
    if is_left_right(char):
        time+=1
        n_left=find_idx(char)
        time+=distance(left[0],left[1],n_left[0],n_left[1])
        left=n_left
    else:
        time+=1
        n_right=find_idx(char)
        time+=distance(right[0],right[1],n_right[0],n_right[1])
        right=n_right
        
print(time)
        

# 20436 / Implementation
# 매우 간단한 단순구현 문제였지만 스스로 미로를 만들었음
# 동시에 칠 수 있으면 시간이 단축 되는 줄 알고 각종 조건문들 덕지 덕지 붙이면서 스스로 망함
# 정확한 문제이해가 매우 중요함을 느낌
# 성우는 두 손을 동시에 움직일 수 없다.!!!!!!!! z o 동시에 못누름!!!! ㅠㅠㅠㅠㅠ
