n=int(input())

file=[]
for i in range(n):
    tmp=input()
    tmp=tmp.split('.')
    file.append(tmp[-1])
# . 뒷부분만 리스트에 저장


unique_file=set(file) # 리스트내 중복 없애고
unique_file=sorted(list(unique_file)) # 정렬해서 고유한 값들만 리스트로 반환 

number=[0]*len(unique_file)

cnt=1

from collections import Counter
file = Counter(file).most_common()
file=sorted(file)

for _ in file:
    print(*_)

# 20291 / Implementation 

# 우선 문제 해결 위해 . 뒷부분으로 확장자에 해당하는 부분만 리스트에 저장 후 
# set 함수 이용해서 리스트 내의 중복을 없앰 
# set 함수는 집합 자료형으로 중복을 허용하지 않으며 순서가 없는 특성이 있다
# 그 이후 collections 함수의 Counter 이용해서 튜플 형태로 값을 저장 해놓음
# Counter -> stored as dictionary keys and their counts are stored as dictionary values
# most_common() -> 요소가 가장 많은것부터 가장 적은 순으로 나열한 튜플 리스트 반환
# 마지막으로 튜플형태릴 * 을 통해 unpacking 하여 각각 출력하도록 함

# 새로 알게 된 함수 -> set() / collections Counter / Counter.most_common() / * -> tuple unpacking

