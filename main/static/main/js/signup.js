

const pass = document.querySelector("#pwd");
const confpass = document.querySelector("#confpwd");
const submit = document.querySelector("#submit");
const passErrorMsg = document.querySelector("#pass-error");

confpass.addEventListener('input', () => {
    passvalue = document.querySelector("#pwd").value;
    passcheck = document.querySelector("#confpwd").value;
    if (passvalue === passcheck) {
        passErrorMsg.style["max-height"] = "0"; 
        submit.removeAttribute("disabled")
        submit.removeAttribute("title")
    }else if(!submit.hasAttribute("disabled"))
    {
        passErrorMsg.style["max-height"] = "500px"; 
        submit.setAttribute("disabled", "");
        submit.setAttribute("title", "Fill Required Fields");
    }else{
        passErrorMsg.style["max-height"] = "500px"; 
    } 
});

pass.addEventListener('input', () => {
    passvalue = document.querySelector("#confpwd").value;
    passcheck = document.querySelector("#pwd").value;
    if (passvalue === passcheck) {
        passErrorMsg.style["max-height"] = "0"; 
        submit.removeAttribute("disabled")
    }
    else if(!submit.hasAttribute("disabled"))
    {
        passErrorMsg.style["max-height"] = "500px"; 
        submit.setAttribute("disabled", "")
    }else{
        passErrorMsg.style["max-height"] = "0"; 
    } 
});


const letter = document.querySelector("#let");
const cap = document.querySelector("#cap");
const spe = document.querySelector("#spe");
const num = document.querySelector("#num");

let letCheck = false;
let capCheck = false;
let speCheck = false;
let numCheck = false;


pass.addEventListener('input', ()=>{
    if(letCheck && capCheck && speCheck && numCheck){
        validations.style["max-height"] = "0";   
    }else{
        validations.style["max-height"] = "500px";   
    }


    if(pass.value.length >= 8){
        letter.classList.remove("invalid");
        letter.classList.add("valid");
        submit.setAttribute("disabled", "")
        letCheck = true;
    }else{
        letter.classList.remove("valid");
        letter.classList.add("invalid");
        submit.setAttribute("disabled", "")
        letCheck = false;
    }

    if(pass.value.match(/[A-Z]/g)){
        cap.classList.remove("invalid");
        cap.classList.add("valid");
        submit.setAttribute("disabled", "")
        capCheck = true;
    }else{
        cap.classList.remove("valid");
        cap.classList.add("invalid");
        submit.setAttribute("disabled", "")
        capCheck = false;
    }

    if(pass.value.match(/\W|_/g)){
        spe.classList.remove("invalid");
        spe.classList.add("valid");
        submit.setAttribute("disabled", "")
        speCheck = true;
    }else{
        spe.classList.remove("valid");
        spe.classList.add("invalid");
        submit.setAttribute("disabled", "")
        speCheck = false;
    }

    if(pass.value.match(/[0-9]/g)){
        num.classList.remove("invalid");
        num.classList.add("valid");
        submit.setAttribute("disabled", "")
        numCheck = true;
    }else{
        num.classList.remove("valid");
        num.classList.add("invalid");
        submit.setAttribute("disabled", "")
        numCheck = false;
    }

})

const validations = document.querySelector(".validations");
// pass.addEventListener("focus", ()=>{
//     validations.style["max-height"] = "500px";  
// })
// pass.addEventListener("blur", ()=>{
//     validations.style["max-height"] = "0";    
// })

const eyes = document.querySelectorAll("#eye");
const eyes_close = document.querySelectorAll("#eye-close");
eyes.forEach(eye => {
    eye.addEventListener("click", ()=>{
            eye.style.display = "none";
            eye.nextElementSibling.style.display = "block";
            eye.previousElementSibling.setAttribute("type", "text");
            
    }
)})

eyes_close.forEach(eye => {
    eye.addEventListener("click", ()=>{
            eye.style.display = "none";
            eye.previousElementSibling.style.display = "block";
            eye.previousElementSibling.previousElementSibling.setAttribute("type", "password");
            
    })
})