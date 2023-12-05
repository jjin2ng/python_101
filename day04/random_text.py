import random

#0 ~ 10 사이 아무 정수나 추출
a = random.randint(0,3)  #0~3 정수 하나 뽑기
print(a)


player = ['손흥민','김민재','황희찬','이강인']
print(player[a])
print(random.choice(player)) #리스트에서 한명 랜덤으로 뽑기


random.shuffle(player) #리스트 섞기
print(player)

c = random.uniform(1.5,2.5) # 주어진 범위에서 무작위 실수



