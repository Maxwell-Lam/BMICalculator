#Maxwell Lam (mvl57)

from flask import Flask, render_template, request

app = Flask(__name__)

def calculateBMI(totalInches, totalPounds):
    totalKg = float(totalPounds) * 0.45
    totalMeters = float(totalInches) * 0.025

    totalMetersSquared = totalMeters * totalMeters
    BMI = totalKg / totalMetersSquared 
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

 
@app.route('/', methods=['GET'])
def squarenumber():
    if request.method == 'GET':
        if(request.args.get('inputInches') == None) or (request.args.get('inputPounds') == None):
            return render_template('squarenum.html')
        elif(request.args.get('inputInches') == '') or (request.args.get('inputPounds') == ''):
            return "<html><body> <h1>Invalid Inputs</h1></body></html>"
        else:
            inputInches = request.args.get('inputInches')
            inputPounds = request.args.get('inputPounds')
            BMI = calculateBMI(inputInches, inputPounds )
            number = calculateWeightClass(BMI)
            return render_template('answer.html', 
                                   squareofnum=BMI, weightClass=number)

if(__name__ == "__main__"):
    app.run(host = '0.0.0.0', port = 7000, debug=True)