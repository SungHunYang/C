# dict 딕셔너리
# 한쌍의 데이터를 하나의 요소로 저장, 관리
# len() 수행시 한쌍을 하나의 요소로 판단하여 카운트 한다.

dic={'사과':'apple','바나나':'banana','키위':'kiwi'}
# 키 : 값 --> key:value  // 키=중복불가 , 값=중복허용
print(dic['사과']) #--> 인덱스 넘버 대신 키를 입력하면 값이 나온다.
'''
dic['사탕']='candy' ---> 값 '추가'
dic['사탕']='CANDY' --> 키가 있으면 값 '변경'
del dic['키위'] --> '요소 삭제'
'''
'''
키 분리
dic.keys() --> 키만 뽑음
kList=list(dic.keys()) #--> 리스트 안에 키 집어넣기 리스트로 변경

값 분리
dic.values() --> 값만 뽑음
vList=list(dic.values())
'''
xList=[10,20,30,40]
xTuple=(10,20,30)
alist=list(dic)
print(alist)
