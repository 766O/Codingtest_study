import sys

num=int(input())
cnt=0

if(num>3):
    solved=[0]*(num+1)
    solved[1]=0
    solved[2]=1
    solved[3]=1
else:
    solved=[0,0,1,1]


for i in range(4,num+1):

    if(i%6==0):
        solved[i]=min(solved[i//3],solved[i//2])+1
    elif(i%3==0):
        solved[i]=min(solved[i//3],solved[i-1])+1 
    elif(i%2==0):
        solved[i]=min(solved[i//2],solved[i-1])+1
    else:
        solved[i]=solved[i-1]+1
    


print(solved[num])

# 1463번 / DP 문제

# 처음에 숫자들 간의 규칙 찾아서 구현하려고 함 -> 실제로 간단한 알고리즘으로는 해결어려움 

# 이전 풀이방법에 있는게 다음 풀이방법에 이용됨을 활용 -> 큰 숫자에 대한 해결책을 작은 숫자들에 대한 정답을 통해 알아보는 방법

#  인덱스 접근시 다음과 같은 오류 발생 *** TypeError: list indices must be integers or slices, not float 
#  인덱스 접근위한 나눗셈시 정수 나눗셈 이용 // 

# DP ->bottom up / top down
# https://codesyun.tistory.com/279
# https://devruby7777.tistory.com/entry/Top-down-DP%EC%99%80-Bottom-up-DP%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90%EA%B3%BC-%EC%9E%A5%EB%8B%A8%EC%A0%90-%EC%93%B0%EB%8A%94-%EA%B2%BD%EC%9A%B0
