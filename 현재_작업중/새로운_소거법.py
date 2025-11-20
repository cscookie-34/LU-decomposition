#입력될 행렬을 다음과 같이 가정 
A=[[None, None, None],
   [None, None, None],
   [None, None, None]]

#1열의 피벗 만들기(3x3행렬이므로, 피벗자리는 주대각 성분)
#최종 목표는 U 만들기(이는 나중에 후진대입법을 편하게 하기 위함)

value =[[None],
        [None],
        [None]]

#이건 방정식의 값들 저장하는거 (첨가행렬로도,가능)


if(A[0][0]==0):
    for i in range(1,3):
        if(A[i][0]!=0):
            #1열 2헹, 3행 탐색 
            #만약 그들중 0이 아닌 값이 나온다면 다음 코드(행교환) 실행) 
            for j in range(3):
                temp = A[0][j]
                A[0][j] = A[i][j]
                A[i][j] = temp


            temp = value[0][0]
            value[0][0] = value[i][0]
            value[i][0] = temp
            #value 에도 적용 

            break
        #헹교환이 이루어졌다면 반복문 break 
    
    
#이제 첫번째 열의 다른 성분들을 모두 0으로 만들기 

if(A[1][0]!=0):
    multinum = A[1][0]
    for i in range(3):
        A[1][i] = A[1][i]-multinum*A[0][i]

    value[1][0] = value[1][0] - multinum*value[0][0]

#A[1][0]이 0이 아닐 경우  

if(A[2][0]!=0):
    multinum = A[2][0]
    for i in range(3):
        A[2][i] = A[2][i]-multinum*A[0][i]

    value[2][0] = value[2][0] - multinum*value[0][0]
#A[2][0]이 0이 아닐 경우  





if(A[1][1]==0):
    if(A[2][1]!=0):
        for i in range(3):
            temp = A[1][i]
            A[1][i] = A[2][i]
            A[2][i] = temp

        temp = value[1][0]
        value[1][0] = value[2][0]
        value[2][0] = temp

#2열의 경우 피벗 바로 아래 있는거 확인-> 0 이 아닌 경우 행교환 


##짠, 상삼각행렬 완성 
Hae_flag = 0
if(A[0][0]==0 or A[1][1]==0 or A[2][2]==0):
    Hae_flag=1