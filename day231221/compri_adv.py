#조건부
a = ['짝' if i%2 else '홀' for i in range(1,10)]
print(a)
b= ['🍎' if i%5==0 else '🍋' for i in range (1,100)]
print(b)
#3의 배수면 피자 아니면 햄버거
c = ['🍕' if i%3==0 else '🍔' for i in range (1,100)]
print(c)

#for 문이 2개 있는게 중첩  [값 for 변수 in 반복가능객체1 for 변수2 in 반복가능객체2]
d= [i * j for i in range(1,10) for j in range(2,9)]
print(d)

e = [i+j for i in 'abc' for j in '123']
print(e)
#온도를 화씨로 변환 celsius=[0,10,20,30,40]
 f = [ (temp *9/5)+32 for temp in range [0,40,10]]
 print(f)