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
def formRoute():
    """This runs the browser and load the form route"""
    formWebPage = render_template("form.html")
    return formWebPage    

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

# serve  the credit page
@app.route("/credithistory.html")
def creditRoute():
    """This runs the browser and load the credit history route"""
    creditWebPage = render_template("credithistory.html")
    return creditWebPage    

# serve thr decision tree page
@app.route("/decision_trees.html")
def dtRoute():
    """This runs the browser and load the decision tree route"""
    dtWebPage = render_template("decision_trees.html")
    return dtWebPage    

# serve  the education page
@app.route("/education.html")
def eduRoute():
    """This runs the browser and load the education route"""
    eduWebPage = render_template("education.html")
    return eduWebPage 

# serve  the gender page
@app.route("/gender.html")
def genderRoute():
    """This runs the browser and load the gender route"""
    genderWebPage = render_template("gender.html")
    return genderWebPage 

# serve  the gender page
@app.route("/k_Nearest_Neighbors.html")
def kNRoute():
    """This runs the browser and load the k_Nearest_Neighbors route"""
    kNWebPage = render_template("k_Nearest_Neighbors.html")
    return kNWebPage 

# serve  the loan page
@app.route("/loanamount.html")
def loanRoute():
    """This runs the browser and load the loanamount route"""
    loanWebPage = render_template("loanamount.html")
    return loanWebPage 

# serve  the logistic-regression page
@app.route("/logistic-regression.html")
def logRRoute():
    """This runs the browser and load the logistic-regression route"""
    logisRWebPage = render_template("logistic-regression.html")
    return logisRWebPage 

# serve  the marriage status page
@app.route("/maritalstatus.html")
def marriageRoute():
    """This runs the browser and load the maritalstatus route"""
    marriageWebPage = render_template("maritalstatus.html")
    return marriageWebPage 

# serve  the model intro page
@app.route("/model_intro.html")
def modelsRoute():
    """This runs the browser and load the model_intro route"""
    modelsWebPage = render_template("model_intro.html")
    return modelsWebPage 

# serve  the neural_networks page
@app.route("/neural_networks.html")
def neuronetRoute():
    """This runs the browser and load the neural_networks route"""
    neuronetWebPage = render_template("neural_networks.html")
    return neuronetWebPage 

# serve  the random_forests page
@app.route("/random_forests.html")
def ranforRoute():
    """This runs the browser and load the random_forests route"""
    ranforWebPage = render_template("random_forests.html")
    return ranforWebPage 

if __name__ == '__main__':
    app.run(debug=True)
