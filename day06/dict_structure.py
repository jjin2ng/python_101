capital = {
    "korea" : "Seoul",
    "china" : "Beijing",
    "malaysia" : "Kuala Lumpur",
    "usa" : "Washington",
}
print(capital["korea"])
pizza_price = {
    "고구마 피자" :17000,
    "페퍼로니 피자" : 14000,
    "하와이안 피자" : 18000,
    "불고기 피자" : 15000,
}

print(pizza_price["불고기 피자"])

japan_travel = {
    "동하" : [ '온천여행','눈싸움'],
    "나은" : ['초밥','기모노'],
    "유진" : ['맛집','디즈니랜드'],
    "동준" : ['당고','도쿄타워'],
}

usa_travel = {
    "동하" :{
        "항공" : "대한항공",
        "가고 싶은 곳" : "뉴욕",
        "먹고 싶은 것" : "햄버거"
    },
    "나은" :{
        "항공" : "제주항공",
        "가고 싶은 곳" : "로스엔젤레스",
        "먹고 싶은 것" : "피자",
    }
}

print(usa_travel["동하"]["먹고 싶은 것"])
print(japan_travel["나은"])

# MBTI
# 당신의 mbti를 입력하세요: ENTJ
# 당신은 외향적이고 직관적이며 T야? 계획적이시군요

MBTI_answer=input("당신의 MBTI가 뭔가요?")
MBTI = {
    "E" : "외향적",
    "I" : "내성적",
    "S" : "직관적",
    "N" : "상상력",
    "T" : "T야",
    "F": "감성적",
    "P": "즉흥적",
    "J": "계획적",
}


print(MBTI[MBTI_answer[0]]+MBTI[MBTI_answer[1]]+MBTI[MBTI_answer[2]]+MBTI[MBTI_answer[3]])