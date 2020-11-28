# Import
from flask import Flask, request
from flask import render_template 
from flask import jsonify


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
# prevent key sorting from jsonify
app.config['JSON_SORT_KEYS'] = False

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
    for key in formResponse.keys():
        for value in f.getlist(key):
            print(key,":",value)

            # process the entries


    
    return render_template('form.html', prediction_text = "Testing")
    
if __name__ == "__main__":
    app.run(debug=True)
