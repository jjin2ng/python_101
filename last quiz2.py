# 반지름 입력 받으면 원 둘레를 출력하는
len1 = int (input("반지름이 얼마죠?"))
pie= 3.14
print(f"반지름이 {len1}이면 원 둘레는 {2*pie*len1}입니다.")

# 반지름 입력 받으면 원 넓이 출력
len2 = int (input("반지름 얼마죠?"))

print(f"반지름이 {len2}이면 원 넓이는 {len2*len2*pie}입니다.")

# 반지름 입력 받으면 구의 부피 출력
len3=int(input("반지름 얼마죠?"))
print(f"반지름이 {len3}이면 부피는 {4/3*pie*len3*len3*len3}입니다.")

# 한 변의 길이를 받으면 정사각형의 둘레와 넓이 출력
len4=int(input("한 변의 길이가 얼마죠?"))
print(f"한 변의 길이가 {len4}이면 정사각형의 둘레는 {4*len4}이고 정사각형의 넓이는 {len4*2}입니다.")
