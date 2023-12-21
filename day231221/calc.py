# + - * / /
def guide():
    print("""사용하실 프로그램을 고르세요.
        1. 덧셈
        2. 뺄셈
        3. 곱셈
        4. 나눗셈
        5. 종료하기 """)


def getNumbers():
    a = int(input("첫 번째 숫자 입력"))
    b = int(input("두 번째 숫자 입력"))
    return a,b
def add(a,b):
	return a + b

def minus(a,b):
	return a - b

def mul(a,b):
	return a * b

def div(a,b):
	return a // b

#1번부터 5번까지 1번은 더하는거
print('계산기 프로그램')
while True:
    guide()
    systemCode = int(input("입력:"))
    if (systemCode == 1) :
        a,b = getNumbers()
        result= add(a,b)
        print(result)
        break

    elif (systemCode == 2) :
        a,b = getNumbers()
        result= minus(a,b)
        print(result)
        break

    elif (systemCode == 3) :
        a,b = getNumbers()
        result= mul(a,b)
        print(result)
        break

    elif (systemCode == 4) :
        a,b = getNumbers()
        result=div(a,b)
        print(result)
        break

    elif (systemCode == 5) :
        break

    else :
        print('다시 입력하세요.')




#일본 계획표 프로그램 0번 여행 필수품 리스트 추가/ 1번 가는 곳 리스트 추가 /2. 먹을거 리스트 추가 /3. 살것 리스트 추가
#현재 필수품 리스트를 보여주고 추가할건 뭔가요? 여권
