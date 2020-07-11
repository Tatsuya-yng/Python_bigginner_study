# BMI計算　「体重(kg) / 身長(m)]

import math

weight = float(input("体重(kg)を入力してください:"))
height = float(input("身長(m)を入力してください:"))

bmi = weight / (height * height)
print("結果:", math.floor(bmi))
