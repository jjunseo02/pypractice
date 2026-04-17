# 교통수단 추천 

"""
거리(km)를 입력받고 적절한 교통수단 추천하기
** if elif else 사용
[추천 기준]
2km 미만: 도보
2km 이상 5km 미만: 자전거
5km 이상 20km 미만: 버스
20km 이상: 지하철
"""

# 거리 정수로 입력받기
# "거리를 입력하세요: "
distance = float(input("거리를 입력하세요: "))
# 만약 거리가 2 미만 < 일시 도보 변수 생성
if distance < 2:
    ride = "도보"
# 2 이상 >= 5미만 < 일시 자잔거 변수 생성
elif distance < 5:
    ride = "자전거"
# 5이상 >= 20미만 < 일시 버스 변수 생성
elif distance < 20:
    ride = "버스"
# 20이상 <= 일시 지하철 변수생성 
else:
    ride = "지하철"
# 거리 출력
print("거리: ", distance, "km")
# "추천 교통수단: " 출력
print(f"추천 교통수단: {ride}")