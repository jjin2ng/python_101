#태어난년도 입력하고 현재 만나이
year1=int(input("몇 년생이세요?"))
year2=int(input("지금은 몇년도죠?"))
result=year2-year1

print(f"{year1}년도에 태어났으면 {result}살이네요.")

#세 개의 숫자 평균 계산기
n1=int(input("숫자 아무거나 입력하세요."))
n2=int(input("숫자 다른거 하나 입력하세요."))
n3=int(input("숫자 또 다른거 하나 입력하세요."))

print(f"세 숫자의 곱은 {n1*n2*n3} 이네요.")

#환율 계산기. krw금액을 받아서 달러 및 엔화로 환산하는 프로그램.
krw=int(input("환전하고 싶은 금액을 입력하세요."))
usd=float("1298.49")
jpy=float("8.79")
print(f"한국돈 {krw}원을 달러로 바꾸면 {krw/usd}달러이고, 엔화로 환전하면 {krw/jpy}엔입니다.")


#km 를 mile 로 변환해라 1km = 0.621371 mile
km = int(input("몇 km를 mile 단위로 바꿀래?"))
mile = float("0.621371")
print(f"{km}를 mile 로 환산하면 {km*mile}입니다.")


#체온 변환기 f=cx59+32
cel=float(input("지금 체온은 어느정도니?"))
print(f"너 체온 {cel}도를 섭씨로 바꾸면 {cel*59+32}야.")

#체질량 키랑 몸무게 받아서 찾아라 bmi = weight / (height **2)
wei = float(input("너 몇 키로지?"))
hei = float(input("키는 얼마지?"))
bmi = float(wei/(hei*2))
print(f"너 키가 {hei}cm고 몸무게가 {wei}kg라고 했으니까 bmi는 {bmi}야.")

#여행 시간 계산기 여행거리와 평균이동속도를 받아 도착까지 걸리는 시간 km 받고 km/h 를 받아서
dis = int(input("도착지까지 거리가 몇 km야?"))
sp = int(input("속도는 어느정도로 달릴건데?"))
print(f"그럼 너 도착까지 걸리는 시간은 {dis/sp} 시 정도겠네.")