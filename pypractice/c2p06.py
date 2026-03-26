# 자료형 변환 활용하기
"""
변수를 지시에 맞게 변경하기
"""

# 아래 두 변수를 정수로 변환하여 총 금액 (price * quantity)구하기
price = "4500"
quantity = "3"

# 문자열을 정수로 바꿔서 계산하기
print(int(price) * int(quantity))

# 아래 두 변수들을 문자열러 연결하여 한 줄로 출력하기

# 스코어 문자열로 변환하여 출력하기
name = "홍길동"
score = 95

print(f"{name}님의 점수는 {str(score)}점입니다.")


n1 = int(input("점수넣어라: "))

n2 = int(input("두 번째 점수 넣어라: "))

print(f"합계: {n1 + n2}")
