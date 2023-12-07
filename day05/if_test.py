# 학생 점수를 입력받고 100점이면 축하합니다. 만점입니다!
# 70점 이상이면 잘하셨습니다.
# 70 미만이면 열공하세요
score = int(input("점수 얼마인가요?"))

if score == 100 :
    print("축하합니다. 만점입니다!")
elif 100 > score >= 70 :
    print("잘하셨습니다.")
else :
    print("열공하세요.")

# 양의 홀수? 양의 짝수? 음의 홀수? 음의 짝수? 아니면 0
nb = int(input("아무 숫자나 입력하세요."))
if nb == 0 :
    print(0)
elif nb > 0 and nb % 2 == 0 :
    print("양의 짝수.")
elif nb > 0 and nb % 2 != 0 :
    print("양의 홀수.")
elif nb < 0 and nb % 2 == 0 :
    print("음의 짝수.")
else :
    print("음의 홀수.")