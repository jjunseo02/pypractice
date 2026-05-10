# print("시작")


# # for _ in range(0):  _ 변수 필없을때
# #     print(_)
# # for char in "hello":
# #     print(char + "_" , end= "")  # end="" 가로로 출력 


# # for value in [10, 20, 30, 40]: # 자료구조 리스트
# #     print(value)

# for val in range(1, 2, 3):
#     print(val ** 2)

# print("끝")


for value in "hello":
    print(value, end="")

print("\n끝")

# 카운트 시키기 
for index, value in enumerate("hello", ):#(스타트 값 설정가능))
    print(f"{index}번째: {value}")