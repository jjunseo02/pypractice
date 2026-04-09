################################# 교수님 코드 모음 (복습)################################
score_list = [90, 60, 100, 70, 100]

total_score = 0

for index in range(len(score_list)):
    total_score += score_list[index]

print(f"total score: {total_score}")






# \n = 엔터키

bar, foo, pos = 3, 5 ,6

print(f"bar: {bar}\nfoo: {foo}\npos: {pos}") # 한줄로 작성하고 가독성 높히기


dataset =[(1,10), (2, 20), (3, 30)]

feature, lable = dataset[0]
print(f"feature: {feature}\nfoo: {lable}")