weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))


bmi = (weight * 703)/(height * height )

if(bmi > 0):
    if(bmi< 18.5):
        print("Classification: Underweight")
        print("Health Risk: Minimal")

    elif(bmi <=24.9):
        print("Classification: Normal weight")
        print("Health Risk: Minimal")

    elif(bmi <=29.9):
        print("Classification: Over weight")
        print("Health Risk: Increased")

    elif(bmi <=34.9):
        print("Classification: Obese")
        print("Health Risk: Very High")

    elif(bmi <=39.9):
        print("Classification: Severly Obese")
        print("Health Risk: Very High")

    elif(bmi > 40):
        print("Classification: Morbidly Obese")
        print("Health Risk: Extremely High")
else:
    print("Enter valid input:")
    