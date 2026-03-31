score = 85
attendance = 92
age = 17
guardian = True
is_vip = False
is_member = True

# 점수가 80 이상 >= 출석률 90 초과 > 식
score >= 80 and attendance > 90

# 점수가 90 이상 >= 출석률 80 이상 >= 인 식
score >= 70 and attendance >= 80

# 나이가 20 이상 >= 이거나 or 보호자기 있는식
age >= 20 or guardian 

# 나이가 19세 미만 < 이거나 or vip 인식
age < 19 or is_vip

# VIP가 아닌식 
not is_vip

# 회원이 아니거나 나이가 20이상 >= 인 식
not is_member or age >= 20

# 점수 90이상 >= 이거나 or 출석률 95 이상 >= 인 식 
score >= 90 or attendance >= 95
