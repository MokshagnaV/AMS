let signup = document.querySelector(".signup");
let login = document.querySelector(".login");
let slider = document.querySelector(".slider");
let formSection = document.querySelector(".form-section");

signup.addEventListener("click", () => {
	slider.classList.add("moveslider");
	formSection.classList.add("form-section-move");
});

login.addEventListener("click", () => {
	slider.classList.remove("moveslider");
	formSection.classList.remove("form-section-move");
});

const eyes = document.querySelectorAll("#eye");
const eyes_close = document.querySelectorAll("#eye-close");
let eyeCheck = true;
eyes.forEach(eye => {
    eye.addEventListener("click", ()=>{
        if(eyeCheck){
            eye.style.display = "none";
            eye.nextElementSibling.style.display = "block";
            eye.previousElementSibling.setAttribute("type", "text");
            eyeCheck = false;
        }
    }
)})

eyes_close.forEach(eye => {
    eye.addEventListener("click", ()=>{
        if(!eyeCheck){
            eye.style.display = "none";
            eye.previousElementSibling.style.display = "block";
            eye.previousElementSibling.previousElementSibling.setAttribute("type", "password");
            eyeCheck = true;
        }
    })
})