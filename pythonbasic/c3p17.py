# 점수 처리 프로그램

"""
국어, 영어, 수학 점수를 입력받고 아래 작업 수행

[지시사항]
1. 각 점수를 변수에 저장
2. 다중 대입으로 과목명을 한 줄에 저장
3. total = 0 으로 초기화
4. +=를 사용하여 총점 계산
5. 평균 계산 후 출력 
"""

# 국어 점수 정수로 입력받기 
# "국어: "
korea = int(input("국어 점수: "))

# 영어 점수 정수로 입력받기
# "영어: "
english = int(input("영어 점수: "))

# 수학 점수 정수로 입력받기
# "수학: "
math = int(input("수학 점수: "))

# 다중대입으로 국, 영, 수 과목명 한줄에 저장식
sub1 , sub2, sub3 = "국어", "영어", "수학"

# total = 0 으로 초기화
total = 0

# 과목명 +=(더하면서 값 저장)으로 총점 계산하기
total += korea
total += english
total += math


# 평균 계산 후 국, 영, 수, 총점 평균 순으로 출력하기 
average = total / 3

print("과목: " + sub1, sub2, sub3)
print("국어: " , korea)
print("영어: " , english)
print("수학: " , math)
print("총점: " , total)
print("평균" , average)

