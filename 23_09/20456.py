from collections import deque

cash=int(input())

stock=list(map(int,input().split()))

def BNP(cash,stock):
    cnt_stock=0
    for i in range(14):
        while(cash>=stock[i]):
            cash=cash-stock[i]
            cnt_stock+=1
        
    return(cash,cnt_stock)

def Timing(cash,stock):
    cnt_stock=0
    for i in range(14):
        if(i>=2 and (stock[i-2]<stock[i-1]<stock[i]) and i<13):
            cash=cash+stock[i+1]*cnt_stock
            cnt_stock=0
           
        if(i>=2 and (stock[i-2]>stock[i-1]>stock[i]) and i<12):
            while(cash>=stock[i+1]):
                cash=cash-stock[i+1]
                cnt_stock+=1
            

            
    return(cash,cnt_stock)

residual,stock_cnt=BNP(cash,stock)
final_BNP=residual+stock[13]*stock_cnt


residual,stock_cnt=Timing(cash,stock)
final_Timing=residual+stock[13]*stock_cnt


if(final_BNP>final_Timing):
    print("BNP")
elif(final_Timing>final_BNP):
    print("TIMING")
else:
    print("SAMESAME")


# 20456 / implemntation
# 구현문제 , 도움없이 혼자서 품 
# 문제 읽고 해당 기능을 하는 함수 구현 하기 
# 문제의 조건 이해하는데 조금 시간 걸림 3일연속 하락 하면 그 다음날 주식을 사는것임
# 반대도 마찬가지 
