# 사용자 입력으로 자기소개 프로그램 만들기

"""
[지시사항]
1. 이름을 입력받아 name 변수에 저장
2. 학번을 입력받아 student_id 변수에 저장
3. 아래 실행 결과와 같은 형식으로 출력
"""
# 이름 name에 입력받기
# "이름을 입력해주세요: "
Name = input("이름을 입력해주세요: ")
# 학번 student_id 에 입력받기 
# "학번 입력해주세요: "
student_id = int(input("학번 입력해주세요: "))

print(f"이름: {Name}")
print(f"학번: {student_id}")
