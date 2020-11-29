
// Radio Buttons
function isRadioButtonChecked(id) {
    return document.getElementById(id).checked;
}

// Number of Dependents Counter
function getNumberFromCounter(id) {
    return document.getElementById(id).valueAsNumber;
}

// Credit History Dropdown
function getCreditValueFromDropdown() {
    return document.getElementById("creditDropdown").value;
}

// Input fields
function inputFields(id) {
    return document.getElementById(id).value;
}

// Term of Loan Dropdown
function getLoanValueFromDropdown() {
    return document.getElementById("termofLoan").value;
}

// Home Location Radio Buttons
function getHomeLocation() {
    if (document.getElementById("urbanPropertyAreaButton").checked === true) {
        return "Urban";
    }

    else if (document.getElementById("semiUrbanPropertyAreaButton").checked === true) {
        return "Semiurban";
    }

    else {
        return "Rural";
    }
}


function getData()
{
    // Gender
    if (isRadioButtonChecked("femaleRadioButton") === true) {
        Gender = "female";
    }

    else {
        Gender = "male";
    }

    // Marital Status
    if (isRadioButtonChecked("yesMarriageButton") === true) {
        Married = true;
    }

    else {
        Married = false;
    }

    // Employment Status
    if (isRadioButtonChecked("yesSelfEmployedButton") === true) {
        Self_Employed = "Yes";
    }

    else {
        Self_Employed = "No";
    }

    // Education status
    if (isRadioButtonChecked("graduateButton") === true) {
        Education = "Graduate";
    }

    else {
        Education = "Not Graduate";
    }

    // Loan Term in Months
    if (getLoanValueFromDropdown() === "30") {
        // 30 years * 12 months in a year
        Loan_Amount_Term = 360;
    }

    else if (getLoanValueFromDropdown() === "15") {
        // 15 years * 12 months in a year
        Loan_Amount_Term = 180;
    }

    else {
        // 10 year term in months
        Loan_Amount_Term = 120;
    }


    // If there are more than 3 dependents, mark as 3+
    if (getNumberFromCounter("dependentCounter") > 3) {
        Dependents = "3+";
    }

    else {
        Dependents = getNumberFromCounter("dependentCounter");
    }


    // Define the remaining variables
    Credit_History = getCreditValueFromDropdown();
    totalIncome = inputFields("totalIncomeInput");
    Property_Area = getHomeLocation();
    LoanAmount = inputFields("loanAmountInput");

    var formResponses = {
        Gender: Gender,
        Married: Married,
        Self_Employed: Self_Employed,
        Education: Education,
        Dependents: Dependents,
        Credit_History: Credit_History,
        totalIncome: totalIncome,
        
        // tab 2 responses
        Property_Area: Property_Area,
        LoanAmount: LoanAmount,
        Loan_Amount_Term: Loan_Amount_Term
    }

    console.log(formResponses);

    return {
        Gender: Gender,
        Married: Married,
        Self_Employed: Self_Employed,
        Education: Education,
        Dependents: Dependents,
        Credit_History: Credit_History,
        totalIncome: totalIncome,
        
        // tab 2 responses
        Property_Area: Property_Area,
        LoanAmount: LoanAmount,
        Loan_Amount_Term: Loan_Amount_Term
    };

};