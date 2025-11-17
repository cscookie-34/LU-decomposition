A = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
#빈 배열 생성 
for i in range(3):
    for k in range(3):
        A[i][k] = float(input())
#빈 배열 A에 입력받은 숫자를 float으로 변환 및 대입 
#다음부터는 둘리틀 방식 사용 (예전에는 가우스)
L=[[1, 0, 0],
   [None, 1, 0 ],
   [None, None, 1]]
#하삼각행렬 
U = [[None, None, None],
     [0,    None, None],
     [0,   0,     None] ]
#상삼각행렬 : 위에서 None 은 아직 정해지지 않은 값들 
flag = 0
#도중에 피벗이 0-> flag 값이 변화해서 LU 분해 불가능함을 알려줌 
U[0][0]=A[0][0]
U[0][1]=A[0][1]
U[0][2]=A[0][2]
#U의 1행 완성
if(U[0][0]==0):
    flag=1
#검증
L[1][0]=A[1][0]/U[0][0]    
U[1][1] = A[1][1]-L[1][0]*U[0][1]
U[1][2] = A[1][2]-L[1][0]*U[0][2]
if(U[1][1]==0):
    flag=1
#U의 2행 완성
L[2][0]=A[2][0]/U[0][0]
L[2][1]=(A[2][1]-L[2][0]*U[0][1])/U[1][1]
U[2][2] = A[2][2]-L[2][0]*U[0][2]-L[2][1]*U[1][2]

print(L)
print(U)

#직전 코드에서 받아온 L, U에 대하여 입력된 연립방정식의 해를 첨가행렬로 표현 
#편의성을 위해 기존 행렬과는 다른 행렬(1 by 3)의 별도의 행렬 사용 
value = [[0],[0],[0]]
#3개 식의 값들을 저장할 행렬 
for i in range(3):
    value[i][0]=float(input())
#입력된 값들을 저장     

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
    value[1][0]=value[1][0]-value[0][0]*multinum

if(L[2][0]!=0):
    multinum=L[2][0]
    value[2][0]=value[2][0]-value[0][0]*multinum
    
if(L[2][1]!=0):
    multinum=L[2][1]
    value[2][0]=value[2][0]-value[1][0]*multinum
#위 연산을 거치면, L 은 기본행렬로 됨. 이제 [U|b]

#이제 U에서 적용 시작
#현재 U의 주대각성분들이 모두 0이 아니라는 보장이 있음 

if(U[2][2]!=1):
    dividenum=U[2][2]
    value[2][0]/=dividenum
    U[2][2]=1

if(U[1][2]!=0):
    multinum=U[1][2]
    value[1][0]=value[1][0]-multinum*value[2][0]
    U[1][2]=0

if(U[0][2]!=0):
    multinum=U[0][2]
    value[0][0]=value[0][0]-multinum*value[2][0]
    U[0][2]=0

if(U[1][1]!=1):
    dividenum = U[1][1]
    value[1][0]/=dividenum
    U[1][1]=1

if(U[0][1]!=0):
    multinum = U[0][1]
    value[0][0]=value[0][0]-multinum*value[1][0]

if(U[0][0]!=1):
    dividenum=U[0][0]
    value[0][0]/=dividenum
    U[0][0]=1

for j in range(3):
    print(value[j][0])


#플래그가 1인 경우 lu 분해를 통하 ㄴ