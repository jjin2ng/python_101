#유저한테 해당 범위를 지정 받는다. 1 ~ n
#n의 범위를 지정해주세요
# 1~n 어떤 정수를 임의로 추출하고 총 5번 기회를 통해서 해당 숫자를 맞추기
# 정답이 맞으면 축하드립니다! 라고 멘트를 쓰고 틀리면 틀렸습니다. 다시 한번 맞춰보세요.

# n 지정은 input
# 범위는 [1, n]

import random
number = int(input("1부터 어디까지 범위 설정할까요?"))
answer = random.randint(1,number)
print(answer)
qst = int(input ("정답이 뭘까요?"))
result = "맞습니다! 축하드립니다!" if answer==qst else "틀렸습니다. 다시 한번 맞춰보세요"
print(result)