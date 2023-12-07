#비밀번호 첫글자 대문자 / 글자수 8개 이상 / 특수문자 포함

password = input("비밀번호 입력하세요.")

if not (password[0].isupper()) :
    print('비밀번호 첫글자를 대문자로 설정해주세요.')
elif len(password) < 8 :
    print('비밀번호를 8 글자 이상으로 설정하세요.')
elif password.isalpha() :
    print('특수문자를 넣어주세요.')
else :
    print('잘했습니다.')

