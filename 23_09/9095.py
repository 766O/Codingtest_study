import sys
input=sys.stdin.readline
num=int(input())

find=[]

for i in range(num):
    find.append(int(input()))

num=max(find)

if num>=3:
    ar=[0]*(num+1)
    ar[0]=0
    ar[1]=1
    ar[2]=2
    ar[3]=4
else:
    ar=[0,1,2,4]


for i in range(4,num+1):
    ar[i]=ar[i-1]+ar[i-2]+ar[i-3]

for i in range(len(find)):
    print(ar[find[i]])

# 9095 / DP
# 점화식을 잘 찾자
