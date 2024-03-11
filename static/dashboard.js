/*
//BMI calculator
function computeBMI() {
// user inputs
    var height = Number(document.getElementById("height").value);
    var weight = Number(document.getElementById("weight").value);
//Perform calculation
    var heightPower = Math.pow(height, 2)
    var BMI = weight/heightPower
    console.log(BMI)

//Display result of calculation
    if(isNan(BMI)){
        document.getElementById("comment").innerText = "Please input numbers for height and weight";
    } else{
        document.getElementById("output").innerText = Math.round(BMI,2);
    }
    var output = BMI
    if (output < 18.5)
        document.getElementById("comment").innerText = "Underweight";
    else if (output >= 18.5 && output <= 25)
        document.getElementById("comment").innerText = "Normal";
    else if (output >= 25 && output <= 30)
        document.getElementById("comment").innerText = "Obese";
    else if (output > 30)
        document.getElementById("comment").innerText = "Overweight";
    else if(isNaN)(output))
        document.getElementById("comment").innerText = "";
}
*/

//BMI
function computeBMI() {
// user inputs
	var height = Number(document.getElementById("height").value);
 	var weight = Number(document.getElementById("weight").value);

//Perform calculation
	var heightPower = Math.pow(height, 2)
	var BMI = weight/heightPower

//Display result of calculation
	if(isNaN(BMI)){
		document.getElementById("output").innerText = "Please input numbers for height and weight";
	}else{
		document.getElementById("output").innerText = Math.round(BMI,2);
	}

	var output = BMI
                if (output < 18.5)
                    document.getElementById("comment").innerText = "Underweight";
                else if (output >= 18.5 && output <= 25)
                    document.getElementById("comment").innerText = "Normal";
                else if (output >= 25 && output <= 30)
                    document.getElementById("comment").innerText = "Obese";
                else if (output > 30)
                    document.getElementById("comment").innerText = "Overweight";
                else if(isNaN(output))
                     document.getElementById("comment").innerText = " ";
}

//Air quality