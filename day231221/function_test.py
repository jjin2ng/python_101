# 중복되는 행동 자동화 시켜주는게 함수

# 출국 시간, 도착시간 이 비행기는 출국시간 __ , 도착시간 __ 비행기입니다.

def planetIme(dep,arr):
    print(f" 이 비행기는 출국시간: {dep} 도착시간: {arr} 비행기입니다.")

planetIme("10:00","13:10")


def greet (name):
    print(f"Hello, {name}!")

greet("Jen")

length = len("Hello")
print(length)

#과일리스트를 2개 받고 합쳐라
def mixedfruits(f1, f2):
    return [i + j for i in f1 for j in f2]

mixedfruits(['apple','banana'],['mango'])

