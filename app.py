# Import
from flask import Flask, request
from flask import render_template 
from flask import jsonify
import pandas as pd
import numpy as np
import joblib 

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
# prevent key sorting from jsonify
app.config['JSON_SORT_KEYS'] = False

#################################################
# Load Model
#################################################
classifier_from_joblib = joblib.load('ml models/logisticRegression.sav')  

#################################################
# Flask Routes
#################################################

# serve  the home page html
@app.route("/")
def homeRoute():
    """This runs the browser and load the index route"""
    indexWebPage = render_template("index.html")
    return indexWebPage  

# serve  the index page html
@app.route("/index.html")
def IndexRoute():
    """This runs the browser and load the index route"""
    indexWebPage = render_template("index.html")
    return indexWebPage  

# serve  the data page
@app.route("/data.html")
def analysisRoute():
    """This runs the browser and load the analysis route"""
    analysisWebPage = render_template("data.html")
    return analysisWebPage    

# serve  the form page
@app.route("/form.html")
def recomendationRoute():
    """This runs the browser and load the recommendation route"""
    recWebPage = render_template("form.html")
    return recWebPage    

@app.route("/predict", methods=["POST"])
def predict():
    """This runs when form response is submited"""

    # get the reponses
    formResponse = request.form
    response_dict = {}
    for key in formResponse.keys():
        for value in formResponse.getlist(key):
            # print(key,":",value)

            # process the entries
            # keys are column names
            # values are column values
            response_dict.update({key :[value]})

    # turn response into dataframe
    responseDf = pd.DataFrame.from_dict(response_dict)

    # prep data
    responseDf["TotalIncome"]=responseDf["TotalIncome"].astype(float)
    responseDf["LoanAmount"]=responseDf["LoanAmount"].astype(float)

    responseDf["Loan_Amount_Term"] = responseDf["Loan_Amount_Term"].str.extract('(\d+)')
    responseDf["Loan_Amount_Term"] = responseDf["Loan_Amount_Term"].astype(float) 
    responseDf["Loan_Amount_Term"] = responseDf["Loan_Amount_Term"]*12

    # data encoding map (same as in data muggling notebook but added credit score category)
    # Data encoding map
    encodingMap = {"Female": 1, "Male": 0,\
                "Yes" : 1, "No": 0,\
                "Y" : 1, "N": 0,\
                "Rural": 0, "Semiurban": 1, "Urban": 2,\
                "Not Graduate": 0, "Graduate": 1,\
                "0": 0, "1": 1, "2": 2, "3+": 3,
                "Poor": 0 , "Fair": 0,"Good": 1,"Excellent": 1}

    response_Encode = responseDf.applymap(lambda x: encodingMap.get(x) if x in encodingMap else x)

    # add feature to work with selected model:
    response_Encode["Log_TotalIncome"]= np.log(response_Encode["TotalIncome"])
    response_Encode["Log_LoanAmount"]= np.log(response_Encode["LoanAmount"])
    response_Encode = response_Encode.drop(columns=["LoanAmount","TotalIncome"])
    
    # Apply model
    prediction = classifier_from_joblib.predict(response_Encode) 
    
    # Convert prediction
    if prediction == 1:
        predictionResult = "Congrats! We think we have a high chance of getting your mortgage loan APPROVED"
    else:
        predictionResult = "Sorry! We think we have a high chance of getting your mortgage loan NOT APPROVED"

    return render_template('form.html', prediction_text = predictionResult)
    
if __name__ == "__main__":
    app.run(debug=True)
