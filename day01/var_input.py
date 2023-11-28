# input은 콘솔에 유저가 입력한 값을 받는 함수

age = input("몇살이세요?")
name = input("이름이 무엇입니까?")
first = input("외향입니까 내향입니까? (E 또는 I 입력)")
second = input(" 직관적입니까? 감각적입니까? ( N 또는 S 입력)")
third = input("감성적입니까? 비인간적입니까? (T 또는 F 입력)")
fourth = input("즉흥적입니까? 계획적입니까 (P 또는 J 입력)")

print(f"{age}살 {name}의 MTBI는 {first}{second}{third}{fourth}")


# 이름 MBTI 나이 XXX 나이의 OOO의 MBTI는 XXXX입니다