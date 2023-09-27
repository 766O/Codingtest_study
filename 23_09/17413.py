import sys
input=sys.stdin.readline
S=input().strip()+' '
# 문자열 앞뒤의 공백문자 제거 ('\n')

flag=0 # 태그안인지 밖인지 여부

stack=[]
result=''


for i in S:
    if i=='<':
        flag=1
        for _ in range(len(stack)):
            result+=stack.pop()
    # 일반 단어 나오다 < 가 나오면 뒤집어서 출력해줘야함 
    # 태그 내부로 전환해주고 
    # 지금까지 들어온 단어들 거꾸로 출력 

    stack.append(i)
        
    if i=='>':
        flag=0
        for _ in range(len(stack)):
            result+=stack.pop(0)
    # > 가 들어오면 태그가 닫혔다는 뜻 / 태그 외부로 전환해주고
    #  가장 처음에 들어왔던 요소부터 "차례대로" 출력
    
    if i==' ' and flag==0:
        stack.pop()
        for _ in range(len(stack)):
            result+=stack.pop()
        result+=' '
    
    # 공백이면서 괄호의 내부가 아닐때 
    # 단어들 사이가 공백으로 구분되있는 경우기 때문에
    # stack 내에 들어온 공백을 먼저 제거해주고
    # 남은 문자들을 역순으로 붙임 
    # 그후에 공백 추가
print(result)

            
            
   
# 17413 / Implementation
# strip 함수 -> 문자열의 시작과 끝에서 공백을 제거한 후 반환
# 만약 strip() 괄호안에 특정 값을 넣으면 해당하는 문자 제거 가능
#     
    
