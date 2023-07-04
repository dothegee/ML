
import pandas as pd
import matplotlib.pyplot as plt

# Linear Regression
# 공부시간에 따른 시험 점수
dataset = pd.read_csv('LinearRegressionData.csv')

# print(dataset.head())

# iloc[row,col]
X = dataset.iloc[:,:-1].values # 처음부터 마지막 컬럼 직전까지의 데이터 (독립 변수)
y = dataset.iloc[:,-1].values # 마지막 컬럼 (종속 변수)

print(X,y)

from sklearn.linear_model import LinearRegression
reg = LinearRegression() # 객체 생성
reg.fit(X,y) # 학습(모델 생성)

y_pred = reg.predict(X) # X에 대한 예측값

print(y_pred)


####################################################
####################################################
# 데이터 시각화

plt.scatter(X,y,color = "blue") #산점도
plt.plot(X, y_pred, color = 'green') #선 그래프
plt.title("Score by hours") # 제목
plt.xlabel('hours')# X축 이름
plt.ylabel('score')# y축 이름
plt.show()


print(f"9시간 공부 했을 때 예상 점수 : {reg.predict([[9]])}")

print(f"{reg.predict([[9],[5],[2]])}")

print(reg.coef_) # 기울기
print(reg.intercept_) # y절편

# 선형회귀의 그래프 식
print("선형회귀 그래프 식")
print(f"y = {reg.coef_}X + {reg.intercept_}")