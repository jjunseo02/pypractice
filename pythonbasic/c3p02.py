###########################################생각이라는걸 하자 ##############################################

"""
거스름돈 계산하기 
물건 가격과 지불 금액을 입력받아 거스름돈 계싼하기
거스름돈은 1000원, 500원 100원 단위로 나눠서 출력

힌트 //(목)과 %(나머지) 활용
"""

price = int(input("물건 가격: "))
paid = int(input("지불 금액: "))

# change = paid - price

# ex1000 = change // 1000
# ex1000s = change % 1000

# ex500 = ex1000s // 500
# ex500s = ex1000s % 500

# ex100 = ex500s // 100

# print(ex1000, ex500 , ex100)

# # //(목) 구하기 체인지 계손 사용하면서 변수 수 줄이기 
# exchange1000 = change // 1000
# change = change % 1000
# # 체인지에 다시 변수주는 이유 = 

# exchange500 = change // 500
# change = change % 500

# exchange100 = change // 100
# change % 100

# print("1000원:", str(exchange1000),"개")
# print("500원: ", str(exchange500), "개")
# print("100원: ", str(exchange100), "개")