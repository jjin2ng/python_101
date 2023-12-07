# 0~100 사이 영어 점수 입력하고 점수에 따라 abcd  나머지는 아쉽게도 탈락이에요.
score = int(input("영어 점수를 입력하세요. "))
if 90 < score <= 100 :
    print('A')
elif 80 < score <=90 :
    print ('B')
elif 70 < score <=80:
    print ('C')
elif 60 < score <=70:
    print ('D')
else:
    print('탈락입니다.')

#각도를 입력하고 예각이면 1 직각이면 2 둔각이면 3 ㅕㅍㅇ각이면 4

ang = int(input("각도를 입력하세요."))
if 0< ang < 90 :
    print('예각입니다.')
elif ang == 90 :
    print('직각입니다.')
elif ang <180 :
    print ('둔각입니다.')
elif ang == 180:
    print('평각입니다.')
else:
    print('잘못 입력하셨습니다.')


#대소문자 바꾸기 문자열을 입력하면 대문잔느 소문자로 솜누자는 대문자로
abc = input("영어 입력하세요.")

if (abc.isupper()):
    print(abc.lower())
else:
    print(abc.upper())



# 국영수 점수 입력하고 한 과목이 100점이면 good 60점 이하면 bad

kor = int(input("국어 점수를 입력하세요."))
eng = int(input("영어 점수를 입력하세요."))
mat = int(input("수학 점수를 입력하세요."))

#90점 이상 a 80점 이상 b 70점 이상 c

if kor == 100 or eng == 100 or mat == 100 :
    print ('Good!')
elif ( kor + eng + mat ) / 3  >=90 :
    print ('A')
elif ( kor + eng + mat ) / 3  >=80 :
    print ('B')
elif ( kor + eng + mat ) / 3  >=70 :
    print ('C')
else:
    print('D')