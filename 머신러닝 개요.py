def get_price(최대금액, 액정파손, 번인, 찍힘, 생활기스, 배터리, 색상):
    적정금액 = 최대금액
    if 액정파손 == True:
        적정금액 -= 150000
    elif 번인 == True:
        적정금액 -= 50000
    
    if 찍힘 >= 3:
        적정금액 -= 30000
    elif 생활기스 == True:
        적정금액 -= 5000

    if 배터리 < 10:
        적정금액 -= 20000

    return 적정금액

# 고전적인 적정금액 산출하는 프로그램(함수)

# 머신러닝은
# 데이터와 거래가격의 상관관계를 찾아
# training data -> learning -> model
# new data => model => prediction