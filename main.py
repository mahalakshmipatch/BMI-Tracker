# BMI
from datetime import date

print(date.today(),"\n")

height = float(input("Enter your height(meters): "))
weight = float(input("Enter your weight(kilograms): "))

bmi = round(weight/(height**2),2)

print("")
print(f"Your BMI: {bmi}")
print("")

if(bmi<18):
    print("You are underweight.")
elif(bmi>25):
    print("You are overweight.")
else:
    print("You are healthy.")

file = open("bmi.txt","a")
record = f"On {date.today()} - BMI: {bmi} (Weight: {weight} kilograms - Height: {height} meters)\n"
file.write(record)
file.close()