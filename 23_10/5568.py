from itertools import permutations
n=int(input())
k=int(input())
arr=[0]*n

for i in range(n):
    arr[i]=(input())

new=list(permutations(arr,k))

#print(new)

number=[]
for i in range(len(new)):
    tmp=''
    for j in range(k):
        tmp=tmp+new[i][j]
    number.append(tmp)

print(len(set(number)))
    
    
# 5568 / Brute Force
# 문제를 이해하면 코딩자체는 쉽다
# 결국 문제에서 원하는것은 n 개의 카드 중에서 k 개만큼 뽑고나서 순서를 매겨 달라는것과 동일
# 이때 중복되지 않는 개수를 구해달라는것
# 즉 조합후에 순서를 매기는것이므로 순열과 같다 -> 순열로 모든 경우의수 구한다음에 set 함수로 중복되는것들을 지우면 끝
# 정수로 다루면 힘들기 때문에 문자로 이용 -> 숫자 붙이기 편하다 , 숫자 붙일때는 tmp ='' 라는 빈 문자열 이용
