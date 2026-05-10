score = 65
attenance_ratio = 75
report = 90

# 불합격 사항 출력하기

if score >= 60:
    if attenance_ratio >= 75:
        if report >= 90:
            print("합격입니다")
        else:
            print("불합격 사유: 래포트")
    else:
        print("불합격 사유: 출석")
else:
    print("불합격 사유: 점수")


# 평탄화 작업하기
# 중첩if문 3단 이상일시 
if score < 60:
    print("불합격 사유: 점수")
elif attenance_ratio < 75:
    print("불합격 사유: 출석")
elif report < 90:
    print("불합격 사유: 래포트")
else:
    print("합격입니다")



