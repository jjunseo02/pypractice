# 수료 판정 

"""
점수, 출석률 입력받고 
점수 80이상 >= 이고 and 출석률 90 초과일시 수료 가능 출력
아닐시에 수료 불가 출력하기
* 비교연산자, 논리 연산자 and 조합하기  
"""

# 점수 정수로 입력받기
# "점수를 입력하세요: "
score = int(input("점수를 입력하세요: "))
# 출석률 점수로 입력받기
# "출석률을 입력하세요: "
attendance = int(input("출석률을 입력하세요: "))
# 만약 점수 80이상 >= 이고and 출석률 90초과 >
# "점수: " , "출석률: ", "수료 가능" 순으로 출력
if score >= 80 and attendance > 90:
    print("점수: " , score)
    print("출석률: " , attendance)
    print("수료 가능")
# 아닐시 "점수: " , "출석률: ", "수료 불가" 순으로 출력
else:
    print("점수: " , score)
    print("출석률: " , attendance)
    print("수료 불가")