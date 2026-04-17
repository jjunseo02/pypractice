# 성적 등급 

"""
점수를 입력받고 등급출력하기
** if elif else 사용하기
[등급 기준]
90 이상: A
80 이상: B
70 이상: C
60 이상: D
60 미만: F
"""

# 점수 정수로 입력받기
# "점수를 입력하세요: "
scoer = int(input("점수를 입력하세요: "))

# 만약 점수 90 이상 >= 일시 "점수 : " , "등급: A" 출력하기
if scoer >= 90:
    print("점수: " , scoer)
    print("등급: A" )
# 만약 점수 80 이상 >= 일시 "점수 : " , "등급: B" 출력하기
elif scoer >= 80:
    print("점수: " , scoer)
    print("등급: B" )
# 만약 점수 70 이상 >= 일시 "점수 : " , "등급: C" 출력하기
elif scoer >= 70:
    print("점수: " , scoer)
    print("등급: C" )
# 만약 점수 60 이상 >= 일시 "점수 : " , "등급: D" 출력하기
elif scoer >= 60:
    print("점수: " , scoer)
    print("등급: D" )
# 만약 점수 60 미만 < 일시 "점수 : " , "등급: F" 출력하기
else:
    print("점수: " , scoer)
    print("등급: F" )

# 한번에 출력도 가능 
# 조건식에 변수 만들기 ex)
# if scoer >= 90:
    # grade = "A"