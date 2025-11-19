A = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
#빈 배열 생성 
for i in range(3):
    for k in range(3):
        A[i][k] = float(input())
#빈 배열 A에 입력받은 숫자를 float으로 변환 및 대입 
#다음부터는 둘리틀 방식 사용 (예전에는 가우스)

value_fixed = [[0],[0],[0]]
#3개 식의 값들을 저장할 행렬 
for i in range(3):
    value_fixed[i][0]=float(input())

    #입력된 값들을 저장     
value1 = [[0],[0],[0]]
for i in range(3):
    value1[i][0] = value_fixed[i][0]

## 주의! 밑 방식은 LU분해 및 이것이 가능한 경우에서의 풀이 


while(True):
    L=[[1, 0, 0],
    [None, 1, 0 ],
    [None, None, 1]]
    #하삼각행렬 
    U = [[None, None, None],
        [0,    None, None],
        [0,   0,     None] ]
    #상삼각행렬 : 위에서 None 은 아직 정해지지 않은 값들 
 
    U[0][0]=A[0][0]
    U[0][1]=A[0][1]
    U[0][2]=A[0][2]
    #U의 1행 완성
    if(U[0][0]==0):
        break
    #검증
    L[1][0]=A[1][0]/U[0][0]    
    U[1][1] = A[1][1]-L[1][0]*U[0][1]
    U[1][2] = A[1][2]-L[1][0]*U[0][2]
    if(U[1][1]==0):
        break
    #U의 2행 완성
    L[2][0]=A[2][0]/U[0][0]
    L[2][1]=(A[2][1]-L[2][0]*U[0][1])/U[1][1]
    U[2][2] = A[2][2]-L[2][0]*U[0][2]-L[2][1]*U[1][2]

    print(L)
    print(U)

    #직전 코드에서 받아온 L, U에 대하여 입력된 연립방정식의 해를 첨가행렬로 표현 
    #편의성을 위해 기존 행렬과는 다른 행렬(1 by 3)의 별도의 행렬 사용 


    #상삼각행렬 : 위에서 None 은 아직 정해지지 않은 값들 
    #여기서는 임시로 위 행렬들을 사용, 나중에 코드 합칠떄는 L, U 이용 

    #[L|V] 에 대하여 L이 기본행렬이 되도록 기본행연산 적용 
    #현재 LU 분해된 꼴애서 L의 주대각성분은 모두 1 이므로, 행교환 불필요
    #아래는 하드코딩으로 함 
    # def PlusMinus(array, i, j):
    #     #매개변수로 행렬, 그 행렬에서 확인할 성분의 위치 i, j
    #     #입력되는 i 값은 무조건 1이상, 즉 1또는 2

    #     if(array[i][j]!=0):
    #         multinum=[i][j]
    #         value[i] = value[i]-value[i-1]*multinum

    if(L[1][0]!=0):
        multinum=L[1][0]
        value1[1][0]=value1[1][0]-value1[0][0]*multinum

    if(L[2][0]!=0):
        multinum=L[2][0]
        value1[2][0]=value1[2][0]-value1[0][0]*multinum
        
    if(L[2][1]!=0):
        multinum=L[2][1]
        value1[2][0]=value1[2][0]-value1[1][0]*multinum
    #위 연산을 거치면, L 은 기본행렬로 됨. 이제 [U|b]

    #이제 U에서 적용 시작
    #현재 U의 주대각성분들이 모두 0이 아니라는 보장이 있음 

    if(U[2][2]!=1):
        dividenum=U[2][2]
        value1[2][0]/=dividenum
        U[2][2]=1

    if(U[1][2]!=0):
        multinum=U[1][2]
        value1[1][0]=value1[1][0]-multinum*value1[2][0]
        U[1][2]=0

    if(U[0][2]!=0):
        multinum=U[0][2]
        value1[0][0]=value1[0][0]-multinum*value1[2][0]
        U[0][2]=0

    if(U[1][1]!=1):
        dividenum = U[1][1]
        value1[1][0]/=dividenum
        U[1][1]=1

    if(U[0][1]!=0):
        multinum = U[0][1]
        value1[0][0]=value1[0][0]-multinum*value1[1][0]

    if(U[0][0]!=1):
        dividenum=U[0][0]
        value1[0][0]/=dividenum
        U[0][0]=1

    for j in range(3):
        print(value1[j][0])
    #만약 LU분해만으로 가능한 경우->자유변수 사용하는 경우는 없음 
    break



##주의! 다음 코드들은 LU 분해 불가-> 가우스-조던 소거법 적용  

value2 = [[0],[0],[0]]
for i in range(3):
    value2[i][0] = value_fixed[i][0]

while(True):
    for i in range(3):
        
        
        
        if(A[i][i]==0):
            
            for j in range(i+1,3):
                if(A[j][i]!=0):
                    temp = value2[i][0]
                    value2[i][0] = value2[j][0]
                    value2[j][0] = temp 
                    #value 행렬에 연산 적용 
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
                zerocount+=1
        if(zerocount==3):
            flag_freecase = 1
            break
        #해당 i열의 모든 성분이 0이라면 이는 자유변수의 도입이 필요한 케이스 

        #이후의 코드들은 그렇지 않음을 전제 

        if(A[i][i]!=1):
            dividenum=A[i][i]
            value2[i][0]=value2[i][0]/dividenum
            for j in range(3):
                A[i][j]=A[i][j]/dividenum
        #만약 해당 주대각성분이 1이 아니라면 해당 성분을 dividenum으로 설정, 해당 행의 모든 성분을 나눠줌 
        
        for j in range(3):
            if(j!=i and A[j][i]!=0):
                multinum = A[j][i]
                value2[j][0] = value2[j][0]-multinum*value2[i][0]
                for k in range(3):
                    temp = multinum*A[i][k]
                    A[j][k] = A[j][k]-multinum*A[i][k]
    for j in range(3):
        print(value2[j][0])
    break
#디버깅용 

#





