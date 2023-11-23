# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height**2)

if bmi<18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi>18.5 and bmi<25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi<30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi<35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")