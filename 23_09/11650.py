'''

import sys

num_case=int(sys.stdin.readline())
coordinate=[]
tmp=[]

coordinate=[sys.stdin.readline().strip() for i in range(num_case)]


x_list=[]
y_list=[]

for i in range(num_case):
    tmp.extend(list((map(int,coordinate[i].split()))))


for i in range(num_case*2):
    if(i%2==0):
        x_list.append(tmp[i])
        print(tmp[i])
    else:
        y_list.append(tmp[i])
        
for i in range(num_case):
    print(sorted(x_list)[i], sorted(y_list)[i])

''' 
# 시간초과 코드

import sys

num_case=int(sys.stdin.readline())

coordinate=[]


for i in range(num_case):
    a,b=map(int,input().split())
    coordinate.append([a,b])

coordinate=(sorted(coordinate))

for i in range(num_case):
    print(coordinate[i][0],coordinate[i][1])
    
#11650 , a,b=map(int,input().split()) -> input 으로 입력받은 문자열에서 split으로 구분하고 map함수 이용해서 정수로 변환
#변환된 정수를 좌표 리스트에 넣어줌
#넣어준후에 sorteds함수 이용해서 정렬
#접근 방법은 맞았는데 첫번째 작성 코드는 시간초과 발생 , x,y 좌표 각각 해서 그런듯
