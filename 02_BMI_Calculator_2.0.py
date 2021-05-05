# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = (weight / (height ** 2))

# Check BMI with the health norms and print out the Type of health you have.

if bmi <= 18.5:
    print(f"Your BMI is {round(bmi)}, and you are Underweight.")
elif bmi <= 25:
    print(f"Your BMI is {round(bmi)}, and you are Normal Weight.")
elif bmi <= 30:
    print(f"Your BMI is {round(bmi)}, and you are Slightly Overweight.")
elif bmi <= 35:
    print(f"Your BMI is {round(bmi)}, and you are Obese.")
else:
    print(f"Your BMI is {round(bmi)}, and you are Clinically Obese.")