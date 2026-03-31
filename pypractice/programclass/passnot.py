# 수료 가는 여부 판정

"""
점수, 출석률 입력받고 점수가 80 이상 >= 이고 and 출석률 90 초과 > 면 "수료가능"
아닐시 "수료 불가"
* 두 조건 모두 만족해야 함 and
if , else 사용
"""

# 점수 정수로 입력받기
# "점수를 입력하세요 : "
score = int(input("점수를 입력하세요 : "))

# 출석률 정수로 입력받기
# "출석률을 입력하세요 : "
attendance = int(input("출석률을 입력하세요 : "))

# 만약 점수 80이상 >= 이고 and 출석률 90초과 > "수료 가능"
# 점수, 출석률, 수료 가능 순서대로 출력
if score >= 80 and attendance > 90:
    print("점수 : " + str(score))
    print("출석률 : " + str(attendance))
    print("수료 가능")

# 아닐시 점수, 출석률, "수료 불가" 순 출력 
else:
    print("점수 : " , str(score))
    print("출석률 : " , str(attendance))
    print("수료 불가")
    