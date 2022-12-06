# BMI Calculator =  W/H**2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi= float(weight) / int(height)**2
bmi_as_int = int(bmi)
print(bmi_as_int)