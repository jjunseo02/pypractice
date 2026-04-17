################################# 교수님 코드 모음 (복습)################################
score_list = [90, 60, 100, 70, 100]

total_score = 0

for index in range(len(score_list)):
    total_score += score_list[index]

print(f"total score: {total_score}")

# \n = 엔터키 활용하기 

bar, foo, pos = 3, 5 ,6

print(f"bar: {bar}\nfoo: {foo}\npos: {pos}") # 한줄로 작성하고 가독성 높히기


dataset =[(1,10), (2, 20), (3, 30)]

feature, lable = dataset[0]
print(f"feature: {feature}\nfoo: {lable}")

################ 소수점 출력하기 #################
# f 스트링 사용시 방법 ex)
print(f"BMI: {bmi:.2f}")
# , 사용시 
print("BMI:", str(round(bmi, 2)))
print(f"BMI: {round(bmi,2)}")

################ if elif ##################
# 출력식이 전부 같을떄
# if 조건식1 or 조2 or 조3:
    #~~~



############# 문자열 속 갯수 세기#############
len()

# ex 비밀번호 속 수가 8자 이상 일시 
if len(password) == 8:
    print()