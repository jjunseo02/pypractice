# BMI 계산기 만들기
"""
키(CM) 몸무게(KG)를 입력받고 BMI 계산하기
BMI 공식 : 몸무게 / 키 의 제곱
주의 : 키는 CM로 입력받지만 공식에서는 m로 변환
힌트: cm > m 변환은 / 100, 제곱은 ** 2를 사용합니다
"""

# 키 인트로 입력받기 
#"키(CM) 를 입력해주세요: "
high = int(input("키(CM) 를 입력해주세요: "))

# 몸무게(KG) 인트로 입력받기
#"몸무게(KG)를 입력하세요: "
weight = int(input("몸무게(KG)를 입력하세요: "))

# 키 cm를 m로 변환하기 
# 키 / 100
highM = high / 100

# BMI 계산하기 
BMI = weight / highM ** 2

# 계산값 출력하기

# 키 출력해서 알려주기
print("키: " + str(high))

# 몸무게 출력해서 알려주기
print("몸무게: " + str(weight))

# BMI 출력하기
print("BMI: " + str(BMI))