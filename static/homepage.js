function dark_light(image) {
   var element = document.body;
   element.classList.toggle("light_mode");
   //document.getElementById("image").src="{{url_for('static', filename='logo_light.png')}}";
   //document.getElementById("toggle").innerHTML = "Dark Mode"
}

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

//terms and conditions - disables submit
function submitTerms(){
document.getElementById("submit").disabled=true;
} //disables submit

//terms and conditions
function activateSubmit(element){
if(element.checked){
document.getElementById("submit").disabled=false;
document.getElementById("terms").value="true";
}
else{
document.getElementById("submit").disabled=true;
document.getElementByid("terms").value="false";
}
document.getElementById("submit").addEventListener("click", isChecked);
}


//settings menu
function settings() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}