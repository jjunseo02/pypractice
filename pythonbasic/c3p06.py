# 시간 변환하기

"""
초(second)를 입력받아 시 분 초로 변환하여 출력하기

힌트 //(몫) %(나머지)를 사용합니다
    1시간에 =3600초, 1분 = 60초

"""
# 시간(초) 정수로 입력받기
# "초를 입력하세요: "
seconds = int(input("초를 입력하세요: "))
 
hour = seconds // 3600 # 입력받은 세컨에서 시간 값 구하는 식
hours = seconds % 3600 # 시간 값에서 나머지값 분 구할때 필요한 변수 

min = hours // 60 # 위에서 나온 값에서 분을 구하는 식 
mins = hours % 60 # 분 구하는 식에서 초를 구하는 나머지 값 

print(str(seconds) + "초")
print(str(hour) + "시간" , str(min) + "분" , str(mins) + "초" )

######## 다른 예시###############

hour = seconds // 3600
seconds = seconds % 3600

mis = seconds // 60
seconds = seconds % 60

print(str(hour) + "시간" , str(mis) + "분" , str(seconds) + "초" )


