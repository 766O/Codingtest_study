import sys

num=int(sys.stdin.readline())

num_list=[]

for i in range(num):
    tmp=int(sys.stdin.readline())
    num_list.append(tmp)

sorted_list=sorted(num_list)

for i in range(num):
    print(sorted_list[i])


# 2751 , 입력을 여러개 받을때 단순히 input 사용하는것이 아닌 sys.stdin.readline() 이용 , https://velog.io/@yeseolee/Python-파이썬-입력-정리sys.stdin.readline    
