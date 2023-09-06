month_day=input()
month,day=map(int,month_day.split(' '))

total_day=0

for i in range(month):
    #import pdb;pdb.set_trace()
    if i==0:
        pass
    elif i == 1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
        total_day=total_day+31
    elif i==4 or i==6 or i==9 or i==11:
        total_day=total_day+30
    else:
        total_day=total_day+28

total_day=total_day+day

result=['SUN','MON','TUE','WED','THU','FRI','SAT']


print(result[total_day%7])

'''
조건문 설정
띄어쓰기 포함되어있는 문자열 받은 후
필요한 정수 따로 따로 꺼내기
'''
