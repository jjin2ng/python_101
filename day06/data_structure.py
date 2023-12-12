# 리스트는 순서가 있고 중복 가능
#a = [1,2,3,4,5,1,2,3,4,5]
#print(a)

# 셋은 순서가 없고, 중복 불가능
#b = {1,2,3,4,5,1,2,3,4,5}
#print(b)

# 셋에 추가하는 add
#b.add('붕어빵')
#b.add('라떼')
#print(b)

#update는 합집합
lunch = {'라면','피자','파스타','샌드위치'}
dinner= {'피자','샌드위치','없음','라떼'}
lunch.update(dinner)
print(lunch)

# 제거 함수 remove or discard
#dinner.remove('없음')    #없는 걸 빼면 에러남
#dinner.discard('라떼')   #없는 걸 빼도 에러 안남
# print(dinner)

#랜덤 제거 함수
#dinner.pop()  #아무거나 하나 빠지는 거
#print(dinner)

#모두 제거 함수
#dinner.clear()
#print(dinner)

#세트 수학적 연산
nation = {'스위스','일본','태국','프랑스'}
europe = {'스위스','프랑스','독일','영국'}

#합집합
uni = nation.union(europe)
print(uni)

#교집합
inter= nation.intersection(europe)
print(inter)

#차집합
diff = nation.difference(europe)
print(diff)

#대칭 차집합
symmetric = nation.symmetric_difference(europe)
print(symmetric)