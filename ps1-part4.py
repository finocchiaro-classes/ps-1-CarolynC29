prior = int(input("Prior arrests:"))
priorLocal = input("Prior arrests for Local ordinance (Y/N):")
age = int(input("Age at release:"))

score = 0

if prior >= 2:
    score += 1
if prior >= 5:
    score +=1
if priorLocal == "Y":
    score += 1
if age >= 18 and age <= 24:
    score += 1
if age >= 40:
    score -= 1

print(f"The recidivism risk score is {score}")
