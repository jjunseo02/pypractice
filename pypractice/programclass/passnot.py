# 수료 가능 여부 판정 

"""
점수와 출석률 입력받고 점수 80 이상 >= 이고 (and) 출석률이 90 초과 > 하면 "수료 가능"
그렇지 않으면 "수료 불가" 출력하기

* 두 조건을 모두 만족해야 함 (and)
if else 문 사용하기
"""

# 점수 정수로 입력받기
# "점수를 입력하세요: "
score = int(input("점수를 입력하세요: "))


# 출석률 정수로 입력받기
# "출석률을 입력하세요: "
attendance = int(input("출석률을 입력하세요: "))


# 만약 점수 80 이상 >= 출석률 90 초과 > 
# 점수, 출석률, "수료 가능" 순으로 출력
if score >= 80 and attendance > 90:
    print("점수 : " , score)
    print("출석률 : " , attendance)
    print("수료 가능")
# 아닐시 점수, 출석률, "수료 불가" 출력
else:
    print("점수 : " , score)
    print("출석률 : " , attendance)
    print("수료 불가")