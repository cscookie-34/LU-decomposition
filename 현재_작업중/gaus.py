A = [[0,0,0],[0,0,0],[0,0,0]]
#빈 행렬 생성 
for i in range(3):
    for j in range(3):
        A[i][j]=float(input())
#행렬 A에 하나씪 값 대입 

for i in range(3):
    
    
    
    if(A[i][i]==0):
        
        for j in range(i+1,3):
            if(A[j][i]!=0):
                for k in range(3):
                    temp = A[i][k]
                    A[i][k] = A[j][k]
                    A[j][k] = temp
                
                break
    
    #이 부분은 처음에 행교환이 필요한지 보는 곳. 
    #먼저 주대각성분이 0인지 확인, 만약 0이라면-> 행교환이 필요
    #동일한 열에 대해, 가장 먼저 만나는 0이 아닌 성분을 지닌 행을 교환 대상으로 
    #위 코드를 실행했음에도, 즉 해당 열의 모든 성분이 0 이라면 자유변수의 도입이 필요한 케이스이므로 이를 flag_freecase
    flag_freecase = 0
    zerocount=0
    for j in range(3):
        if(A[j][i]==0):
            zercount+=1
    if(zerocount==3):
        flag_freecase = 1
    #해당 i열의 모든 성분이 0이라면 이는 자유변수의 도입이 필요한 케이스 

    #이후의 코드들은 그렇지 않음을 전제 

    if(A[i][i]!=1):
        dividenum=A[i][i]
        for j in range(3):
            A[i][j]=A[i][j]/dividenum
    #만약 해당 주대각성분이 1이 아니라면 해당 성분을 dividenum으로 설정, 해당 행의 모든 성분을 나눠줌 
    
    for j in range(3):
        if(j!=i and A[j][i]!=0):
            multinum = A[j][i]
            for k in range(3):
                temp = multinum*A[i][k]
                A[j][k] = A[j][k]-multinum*A[i][k]
            

        


