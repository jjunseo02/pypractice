# BMI 판정

"""
키 몸무게 입력받아 BMI 계산하고 판정 결과 출력하기
** if elif else 사용 
BMI = 몸무게 / (키 제곱**)
(키는 cm로 입력받아서 m로 변한 필요 cm / 100)
[판정 기준]
BMI 18.5 미만: 저체중
BMI 18.5 이상 23 미만: 정상
BMI 23 이상 25 미만: 과체중
BMI 25 이상: 비만
"""

# 몸무게 실수로 입력받기
# "몸무게를 입력하세요 (kg): "
weight = float(input("몸무게를 입력하세요 (kg): "))

# 키 실수로 입력받기
# "키를 입력하세요 (cm): "
height = float(input("키를 입력하세요 (cm): "))

# 키 m로 변환하기 
m_height = height / 100
# BMI 공식 만들기
bmi = weight / (m_height ** 2)

# 만약 bmi 18.5 미만 < "저체중"
if bmi < 18.5:
    bmilist = "저체중"
# bmi 23 < 미만 "정상"
elif bmi < 23:
    bmilist = "정상"
# bmi 25 < 미만 "과체중"
elif bmi < 25:
    bmilist = "과체중"
# 전부 아닐시 "비만"
else:
    bmilist = "비만"
# (키: cm 몸무게: kg) bmi 수치, 판정결과 순으로 출력하기

print(f"키: {height}cm, 몸무게: {weight}kg")
print(f"BMI: {bmi:.2f}")
print(f"판정: {bmilist}")

# (f"BMI: {round(bmi,2)}")
