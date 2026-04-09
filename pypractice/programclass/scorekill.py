# 점수 처리 프로그램

"""
국어 영어 수학 점수 입력받고 아래작업수행
입력 받은 각 점수 변수에 저장
다중대입 사용 sub1 snb2 sub3 변수에 국어 영어 수학 저장
total = 0 으로 초기화
+=를 사용하여 총점 계산
과목명 각 점수 총점 평균 출력
"""


# 국어 점수 정수로 입력받기
# "국어 점수: "
korea = int(input("국어 점수: "))


# 영어 점수 정수로 입력받기
# "영어 점수: "
english = int(input("영어 점수: "))

# 수학 점수 정수로 입력받기
# "수학 점수: "
math = int(input("수학 점수: "))

# 다중대입 sub1, sub2, sub3, 에 각 국, 영, 수 입력하기
sub1, sub2, sub3, = korea, english, math 
subject = ("국어 영어 수학")

# 총점 total = 0 으로 시작
total = 0

# 국 영 수 점수 하나씩 (+=) 로 누적하기
total += sub1
total += sub2
total += sub3


# 평균구하기 식 총점 / 3과목
aver = total / 3

# 출력순서 국 > 영 > 수 > 총점 > 평균 구하기
print(f"과목: {subject}")
print(f"국어: {sub1}")
print(f"영어: {sub2}")
print(f"수학: {sub3}")
print(f"총점: {total}")
print(f"평균: {aver}")