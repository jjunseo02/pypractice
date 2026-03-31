# 성적 등급 

"""
점수 입력받고 등급출력하기
if/elif/else  사용하기

[등급기준]
90 이상 >= A
80 이상 >= B
70 이상 >= C
60 이상 >= D
60 미만 < F
"""

# 점수 정수로 입력받기
# "점수를 입력하세요: "
score = int(input("점수를 입력하세요: "))

# 만약 90 이상 >= 
# 등급 "A" 설정하기
if score >= 90:
    grade = "A"
# 80 이상 >=
# 등급 "B" 설정하기
elif score >= 80:
    grade = "B"
# 70 이상 >= 
# 등급 "C" 설정하기
elif score >= 70:
    grade = "C"

#60이상 >=
# 등급 "D" 설정하기
elif score >= 60:
    grade = "D"

# 60 미만 <
# 등급 "F" 설정하기
else:
    grade = "F"

print("점수:" , score)
print("등급:" , grade)