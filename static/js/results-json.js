
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
        return "urban";
    }

    else {
        return "suburban";
    }

}


function getData()
{

    return {
        // tab 1 responses
        genderF: isRadioButtonChecked("femaleRadioButton"),
        marriageY: isRadioButtonChecked("yesMarriageButton"),
        selfEmployedY: isRadioButtonChecked("yesSelfEmployedButton"),
        graduatedY: isRadioButtonChecked("graduateButton"),
        numberDependents: getNumberFromCounter("dependentCounter"),
        creditHistory: getCreditValueFromDropdown(),
        totalIncome: inputFields("totalIncomeInput"),
        
        // tab 2 responses
        homeLocation: getHomeLocation(),
        loanAmount: inputFields("loanAmountInput"),
        creditHistory: getLoanValueFromDropdown(),


    }
};