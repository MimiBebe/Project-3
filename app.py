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
    """This runs the browser and load the data route"""
    analysisWebPage = render_template("data.html")
    return analysisWebPage    

# serve  the form page
@app.route("/form.html")
def recomendationRoute():
    """This runs the browser and load the form route"""
    recWebPage = render_template("form.html")
    return recWebPage    

# serve the route to get the form input and return the prediction
@app.route("/response", methods=["POST"])
def formResponse():
    """This runs when form response is submited"""
    response_dict = request.json
    print(response_dict)

    # turn response into dataframe
    responseDf = pd.DataFrame.from_dict(response_dict)

    # Casting strings to int or floats
    responseDf["totalIncome"]=responseDf["totalIncome"].astype(float)
    responseDf["LoanAmount"]=responseDf["LoanAmount"].astype(float)


    # data encoding map (same as in data muggling notebook but added credit score category)
    # Data encoding map
    encodingMap = {"Female": 1, "Male": 0,\
                "Yes" : 1, "No": 0,\
                "Y" : 1, "N": 0,\
                "Rural": 0, "Semiurban": 1, "Urban": 2,\
                "Not Graduate": 0, "Graduate": 1,\
                "0": 0, "1": 1, "2": 2, "3+": 3}

    response_Encode = responseDf.applymap(lambda x: encodingMap.get(x) if x in encodingMap else x)
    
    # Apply model
    prediction = classifier_from_joblib.predict(response_Encode) 
    
    # Convert prediction
    if prediction == 1:
        predictionResult = "Approved"
    else:
        predictionResult = "Sorry!"

    # Print to terminal
    print(predictionResult)

    return predictionResult

# serve  any html here
# @app.route("/form.html")
# def recomendationRoute():
#     """This runs the browser and load the form route"""
#     recWebPage = render_template("form.html")
#     return recWebPage    



if __name__ == '__main__':
    app.run(debug=True)
