
gibon =[[1, 0, 0], 
        [0, 1, 0], 
        [0, 0, 1]]

a = [[0, 0, 0], 
     [0, 0, 0], 
     [0, 0, 0]]
#기본행렬, 빈 행렬 생성

L = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
gibonarrays = []
#기본행렬들 저장할 빈 리스트 생성 

for i in range(3):
    for j in range(3):
        a[i][j] = float(input())
#빈 행렬에 값 입력 ->  LU 분해의 대상이 될 행렬 
class Gibon:
    def __init__(self, name):
        self.default=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.name = name 
    def change(self, i, j):

        self.default[i][i]=0
        self.default[j][j]=0
        self.default[i][j]=1
        self.default[j][i]=1

    def multiple(self, i, multinum ):

        self.default[i][i]=1/multinum

    def plusminus(self, i,k, multinum ):

        self.default[k][i]=-multinum
        
def inverse(cal):
    """기본 행렬의 역행렬 계산"""
    inv = [[0, 0, 0] for _ in range(3)]
    
    # 대각선 요소 복사 및 역수 계산
    for i in range(3):
        if cal[i][i] != 0 and cal[i][i] != 1:
            # 스케일링 행렬의 역행렬
            inv[i][i] = 1 / cal[i][i]
        else:
            inv[i][i] = cal[i][i]
    
    # 비대각선 요소 처리
    for i in range(3):
        for j in range(3):
            if i != j:
                if cal[i][j] != 0:
                    # 행 교환 행렬은 자기 자신이 역행렬
                    if cal[i][i] == 0:
                        inv[i][j] = cal[i][j]
                    else:
                        # 행 덧셈 행렬의 역행렬 (부호 반대)
                        inv[i][j] = -cal[i][j]
    
    return inv

def arraymultiple(array1, array2):
    resultarray=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        #행 
        for j in range(3):
        #열
            result=0
            for k in range(3):
                result +=array1[i][k]*array2[k][j]
            resultarray[i][j] = result 


            # i는 행 번호 k 가 증가 하면서 열 바뀜, j는 열, k 가 바뀌면서 행 변화 
        #헹과 열이 고정되어 있음
    return resultarray


count=0

for i in range(3):
    judaegak = a[i][i]
    
    #주대각 성분 확인 
    if(judaegak==0):
        for j in range(3):
            if(i!=j and a[j][i]!=0):
                for k in range(3):
                    temp = a[i][k]
                    #교환대상의 값 저장
                    a[i][k] = a[j][k]
                    a[j][k] = temp  
                defaultcal=Gibon(name=f"e_{count}")
                defaultcal.change(i,j)
                gibonarrays.append(defaultcal)
                count+=1
                break
        judaegak=a[i][i]

    if(judaegak!=1):
        #주대각 성분이 1이 아닌 경우 
        dividenum = judaegak
        for j in range(3):
            a[i][j] = a[i][j]/dividenum
        defaultcal= Gibon(name=f"e_{count}")
        defaultcal.multiple(i,dividenum )
        gibonarrays.append(defaultcal)
        count+=1
            #1이 아닌 경우: 그 숫자로 해당 행의 성분을 모두 나눔 
    #i 행의 주대각성분이 이제 1 : 해당 주대각성분의 열 확인 
    for k in range(3):
        if(i!=k and a[k][i]!=0 and k>i):
            multinum = a[k][i]
            for j in range(3):
                a[k][j]=a[k][j]-multinum*a[i][j]
            defaultcal = Gibon(name=f"e_{count}")
            defaultcal.plusminus(i, k, multinum )
            gibonarrays.append(defaultcal)
            count+=1

    

for array in gibonarrays:
        array.default = inverse(array.default)
    #역행렬 만들기 
    
for array in gibonarrays:
        L = arraymultiple(L, array.default)
    


for array in gibonarrays:
    print(array.default)

print(L)
print(a)
result = arraymultiple(L, a)
for row in result:
    print([round(x, 2) for x in row])