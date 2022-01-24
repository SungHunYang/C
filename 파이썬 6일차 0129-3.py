
# 가변 인자
# 몇개 넣어야 될지 모를때 쓰는것 
def f1(*x):  # 인자 앞에 *하면 몇개 넣을지 모른다
    print(x)
    print(type(x))


f1(10)

def f(*x):
    res=0
    for v in x:
        print('출력 ...',v)
        res+=v
    return res

# 학생들의 평균 구함

def stuAvg(*x):
    res=0
    cnt=len(x)
    for v in x:
        res+=v
    print('이 반 학생은 총',cnt,'명')
    print('총점은',res,'점이고, 평균은',res/cnt,'점 입니다')

stuAvg(10, 90, 87, 56, 77)    

def findMax(*x):
    big=x[0]
    bIndex=0
    for i in range(len(x)):
        if big<x[i]:
            big=x[i]
            bIndex=i
    print(bIndex+1,'번째로 입력된 [',big,'] 이 가장 큰 데이터 입니다.')
findMax(1123,123,3,3123,1534,4566,2134)
        








    
