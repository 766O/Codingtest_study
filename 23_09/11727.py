import sys
input=sys.stdin.readline
num=int(input())

if num>=3:
    ar=[0]*(num+1)
    ar[0]=0
    ar[1]=1
    ar[2]=3
else:
    ar=[0,1,3]
    
for i in range(3,num+1):
    if i%2 !=0:
        ar[i]=ar[i-1]*2-1
    else:
        ar[i]=ar[i-1]*2+1

print(ar[num]%10007)

# 11727 / DP
# 직접 그림그리면서 경우의 수 찾은후에 관계를 찾았는데 정석 풀이법이랑 다름
# 홀수에서 짝수번 인덱스가 될때는 2*n+1 배 되고 (ex 1일때 경우의 수 1 -> 2일때 경우의 수 3)
# 짝수에서 홀수번 인덱스가 될때는 2*n-1 배가 됨(ex 2일때 경우의수 3 -> 3일때 경우의 수 5)

# 정석 풀이법 -> 일반화된 점화식을 구한다
# https://didu-story.tistory.com/223

# 너무 억지로 끼워 맞춰서 푼 문제 ,작은 문제들로 나누어 동적 프로그래밍으로 풀이하는걸 생각하면서 접근하기
