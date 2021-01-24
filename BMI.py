# Weight = w, Height = h

w = input("Pls input your weight : ")
w = float(w)
h = input("Pls input your height : ")
h = float(h)
BMI = w / (h*h)
print(BMI)
if BMI < 18.5:
    print('體重過輕')
elif BMI >=18.5 and BMI < 24:
    print("正常範圍")
elif BMI >= 24 and BMI < 27:
    print('過重')
elif BMI >= 27 and BMI < 30:
    print("輕度肥胖")
elif BMI >= 30 and BMI < 35:
    print("中度肥胖")
else:
    print("重度肥胖")

