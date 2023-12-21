#문제1: 리스트 컴프리헨션 이용한 짝수 생성

#컴프리헨션을 사용하자 (쉽게 리스트 데이터 조작 가능) how to []
#for 문 = [i for i in range(10)]
#1부터 20까지의 숫자 중에서 짝수만 포함하는 리스트 컴프리헨션을 사용하여 만드세요 예상답[2,4,6,---,20]

    a = [i for i in range(20) if i % 2 == 0]
    print(a)



# 문제2: 조건을 포함한 리스트 컴프리헨션
list = [1,2,3,4,5,6,7,8,9,10]
b = [i for i in list if i > 5]


fruits = ["apple","banana","cherry","date"]
c = [i[0] for i in fruits]

# 문제3: 문자열 처리를 위한 리스트 컴프리헨션
# 문자열 리스트 ["apple", "banana", "cherry"] 의 각 단어를 대문자로 변환하여 새로운 리스트를 만드세요

sq = [i**2 for i in range(1,6)]


# 문제5 문자열 리스트 ["hello", "world", "python", "programming"] 에서 각 단어의 길이의 구하여 새로운 리스트를 만드세요.
words=["hello", "world", "python", "programming"]
lenwords = [len(i) for i in words]

lowerwords = ["apple","banana","cherry"]
upperwords = [i.upper() for i in lowerwords]


answer= [i**2 for i range (1,9,2)]
