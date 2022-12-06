''' 
Write a program that interprete the Body Mass Index (BMI) based on a user height and weight.
It should tell them the interpretation of their BMI based on the BMI Value.

* Under 18.5 they're over-weight.
* Over 18.5 but below 25 they've a normal weight.
* Over 25 but below 30 they're overweight.
* Over 30 but below 35 they're obese.
* above 35 they're clinically obese.
'''

weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))

bmi = round(weight / height ** 2)
if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you're underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you've a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you're overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you're obese.")
else:
    print(f"Your BMI is {bmi}, you're clinically obese")
