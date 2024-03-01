def calculateBMI(totalInches, totalPounds):
    totalKg = float(totalPounds) * 0.45 
    totalMeters = float(totalInches) * 0.025

    totalMetersSquared = totalMeters * totalMeters
    BMI = totalKg / totalMetersSquared 
    BMI = round(BMI, 2)
    return(BMI)

def calculateWeightClass(BMI):
    if (BMI < 18.5):
        return "Underweight"
    elif (BMI < 25.0):
        return "Normal Weight"
    elif (BMI < 30.0):
        return "Overweight"
    else: 
        return "Obese"
    

    