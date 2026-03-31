# 할인 가격 계산
"""
상품 3개 원래 가격과 할인율을 보고 할인 가격 계산후 총 결제 금액 구하기
힌트: 할인가격 = 원래가격 * (1 - 할인율)
    총액은 += 연산자로 누적합니다.
"""

total = 0

# 상품 1: 노트북 1200000원, 10% 할인
item1 = 1200000
discount1 = 0.1
price1 = item1 * (1 - discount1)
# item1 - (item1 * discount1)

# 상품 2: 마우스 35000원, 20% 할인 
item2 = 35000
discount2 = 0.2
price2 = item2 * (1- discount2)

# 상품 3: 키보드 55000원, 15% 할인 
item3 = 55000
discount3 = 0.15
price3 = item3 * (1 - discount3)


# 총액 구하기
total += price1
total += price2
total += price3

# 각 상품의 할인 가격을 계산하고 총액 구하기
print("노트북" , int(price1), "원")
print("마우스" ,int(price2) , "원")
print("키보드" , int(price3) , "원")
print("총 결제 금액" ,int(total) , "원")



