# 구구단 만들기

"""
단수를 입력받고 해당 구구단 출력하기
** for + range() 사용하기
"""

# 몇단인지 정수로 입력받기 
# "몇 단을 출력할까요?: "
dan = int(input("몇 단을 출력할까요?: "))

# for range 사용하여 구구단 만들기 (, ,)
for i in range(1, 10):
    print(dan , "x", i , "=", dan * i)               # 프린트 i
