kor = int(input("국어 점수를 입력하세요."))
eng = int(input("영어 점수를 입력하세요."))
mat = int(input("수학 점수를 입력하세요."))

#90점 이상 a 80점 이상 b 70점 이상 c


if kor == 100 or eng == 100 or mat == 100 and ( kor + eng + mat ) / 3  >=90 :
    print (''A')
elif kor == 100 or eng == 100 or mat == 100 and ( kor + eng + mat ) / 3  >=80 :
    print ('B')
elif kor == 100 or eng == 100 or mat == 100 and ( kor + eng + mat ) / 3  >=70 :
    print ('C')
else:
    print('D')