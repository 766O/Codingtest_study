import sys

num_case=int(sys.stdin.readline())

coordinate=[]

for i in range(num_case):
    b,a=map(int,input().split())
    coordinate.append([a,b])
    
coordinate=sorted(coordinate)

for i in range (num_case):
    print(coordinate[i][1],coordinate[i][0])
    
# 11651 , 11650 문제오 동일하지만 y기준 정렬을 실행해야되기때문에 기준점이 되는 y 를 앞자리로 받아놓고 출력시에만 뒤집기
