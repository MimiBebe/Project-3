
// Radio Buttons
function isRadioButtonChecked(id) {
    return document.getElementById(id).checked;
}

// Number of Dependents Counter
function getNumberFromCounter(id) {
    return document.getElementById(id).valueAsNumber;
}

// Dropdown
function getValueFromDropdown(id) {
    return document.getElementById(id).value;
}

// Input fields



function getData()
{

    return {
        genderF: isRadioButtonChecked("femaleRadioButton"),
        marriageY: isRadioButtonChecked("yesMarriageButton"),
        selfEmployedY: isRadioButtonChecked("yesSelfEmployedButton"),
        graduatedY: isRadioButtonChecked("graduateButton"),

        numberDependents: getNumberFromCounter("dependentCounter"),
            
        
        // creditScore: getValueFromDropdown("creditDropdown"),
    };



}