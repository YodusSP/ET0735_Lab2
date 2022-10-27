def calculate_bmi(weight, height):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = float(weight)/ (float(height)*float(height))

    print(bmi)

    if(bmi<18.5):
        print("Under Weight")
    elif (bmi<25.0):
        print("Normal Weight")
    else:
        print("Overweight")

calculate_bmi(weight= 57, height=1.73)