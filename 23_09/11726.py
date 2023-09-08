import sys
input=sys.stdin.readline
num=int(input())

if(num>=3):
    ar=[0]*(num+1)
    ar[1]=1
    ar[2]=2
else:
    ar=[0,1,2]

if(num>=3):
    for i in range(3,num+1):
        ar[i]=ar[i-1]+ar[i-2]

print(ar[num]%10007)

#11726 / DP
#처음으로 완벽하게 풀어냄 ,문제를 해석하면 단순한 피보나치 문제임 
