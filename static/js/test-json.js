function isRadioButtonChecked(id)
{
    return document.getElementById(id).checked;
}

function getNumberFromCounter(id)
{
    return document.getElementById(id).valueAsNumber;
}

function getValueFromDropdown(id)
{
    return document.getElementById(id).value;
}

function getData()
{

    return {
        genderF: isRadioButtonChecked("femaleRadioButton"),
        marriageY: isRadioButtonChecked("yesMarriageButton"),
        numberDependents: getNumberFromCounter("dependentCounter"),
        // creditScore: getValueFromDropdown("")

    };



}