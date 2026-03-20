# 실무 파일 헤더 주석하기

# --------------------------
# 파일명 입력받기
file = input("파일명을 입력해주세요: ")

# 작성자 입력받기
who = input("작성자를 입력해주세요: ")
# 학번 입력받기
num1 = input("학번을 입력해주세요: ")
# 작성일 입력받기
W_day = input("작성일을 입력해주세요: ")
# 설명 입력받기
whatIs = input("설명을 입력해주세요: ")

print("-"*30)
print(f"파일명: {file}")
print(f"작성자: {who}")
print(f"학번: {num1}")
print(f"작성일: {W_day}")
print(f"설명: {whatIs}")
print("-" * 30)

# 파일해더 주석 작성 완료 띄우기
print("파일 헤더 주석 작성 완료!")