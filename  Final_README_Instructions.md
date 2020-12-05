## Final Project: Machine Learning - Predicting Mortgage Approval </br>

## Group 7 Team Members: 
Amanda Enstad, Chi Tran, Matt Russell, Barbara MacGregor

Website: https://loanpredictor-abcm.herokuapp.com/

### Requirements Met: </br>

<ul>
                <li>scikit-learn and other Machine Learning Libraries</li>
                <li>Applications used include Pandas, HTML/CSS/Bootstrap, MatPlotLib, Flask, joblib</li>
                <li>Website that summarizes our work</li>
                <li>Hosting our website on Heroku</li>
              </ul>

## About the Data </br>

### Data Munging </br>

We used .csv files from a Kaggle database, one for validation data and one for training/testing. We then extracted, transformed the data via Pandas ,created visualizations you will see on the website via MatPlotLib and wrote the transformed datasets into new .csv files that we used to apply various ML models on.

Assumptions

<ul>
                <li>Our data set didn’t define what a credit history of 0 or 1 means. We decided to assume that a score of 0 equals “Poor” or “Fair” credit, and a score of 1 equals “Good” or “Excellent” credit based on examination of the Decision Tree paths, where “1” was associated with loan approval and “0” with denial.</li>
                <li>The data set doesn’t define whether “Graduate” refers to high school or college. Based on the high percentage of graduates in the data set, we are assuming “Graduate” to mean “High School Graduate”</li>
                <li>For “Dependents”,”Self-employed” and “Credit history”, we assume missing entries meant “0” or “No” and fill the data accordingly.</li>
                <li>For missing values in “Gender” and “Loan amount”, we dropped these entries since it could not be filled with high confidence.</li>
              </ul>

### Training Data (6 pages) </br>

We also wanted to dig deeper on different data segments to see if there were significant differences between these segments earning loan approval or not and determine if we could generate any hypotheses. The segments we showed examples for were: 
<ul>
                <li>Credit History</li>
                <li>Loan Amount</li>
                <li>Gender</li>
                <li>Education</li>
                <li>Marital Status</li>
              </ul> 

### Logistic Regression Model </br>

We looked at multiple models and tested multiple trials for each one but ultimately decided to use Logistic Regression for our model. To increase accuracy, we improved log transformations of Total Income and Loan Amount to reduce the influence of outliers. 

## Mortgage Approval Website: Functionality and Capabilities. </br>

### Hosted on Heroku </br>

We are using Heroku as our website host. We utilized a Flask server to run our Machine Learning Model to determine whether or not people who fill out our form qualify for a mortgage loan. 

### Form Pages</br>

This page utilizes a multi-step form, allowing the user to see if they would likely qualify for a loan via our Machine Learning Model. The output will either be "Sorry, you didn't qualify" or "Congrats! You qualify!" From this page, you will be able to choose options to learn more about the models we tested or specific data segments.</br>

### Our Models (5 pages) </br>

We tested out several models and results and explanations are desribed on these pages. The tests we used include:
<ul>
                <li>Logistic Regression  (we chose this model to predict user approval status)</li>
                <li>KNeighbors Classifier</li>
                <li>Decision Trees</li>
                <li>Random Forests</li>
                <li>Neural Networks</li>
              </ul>


