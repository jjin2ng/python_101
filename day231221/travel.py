def guide():
    print("""여행 계획 프로그램
0번. 여행 필수품 리스트
1번. 가는 곳 리스트
2번. 먹을것 리스트
3번. 살것 리스트
4번. 종료 """)

def necessity(list):
    print(f"현재 리스트: {list}")
    item = input("추가할리스트:")
    list.append(item)


print('일본 여행 프로그램')
while True:
    necessityList=[]
    placeList=[]
    foodList=[]
    shoppinglist=[]

    guide()
    travleCode = int(input("번호를 고르세요:"))
    if (travleCode == 0) :
        necessity(necessityList)

