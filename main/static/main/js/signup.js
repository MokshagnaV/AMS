

const pass = document.querySelector("#pwd");
const confpass = document.querySelector("#confpwd");
const submit = document.querySelector("#submit");

submit.addEventListener('click', () => {
    passvalue = document.querySelector("#pwd").value;
    passcheck = document.querySelector("#confpwd").value;
    if (passvalue !== passcheck) {
        alert("Password and Confirm Password doesn't ")
    }
})

confpass.addEventListener('input', () => {
    passvalue = document.querySelector("#pwd").value;
    passcheck = document.querySelector("#confpwd").value;
    console.log(passcheck, passvalue)
    if (passvalue === passcheck) {
        submit.removeAttribute("disabled")
    } else if(!submit.hasAttribute("disabled"))
    {
        submit.setAttribute("disabled", "");
    }
});

pass.addEventListener('input', () => {
    passvalue = document.querySelector("#confpwd").value;
    passcheck = document.querySelector("#pwd").value;
    console.log(passcheck, passvalue)
    if (passvalue === passcheck) {
        submit.removeAttribute("disabled")
    } else if(!submit.hasAttribute("disabled"))
    {
        submit.setAttribute("disabled", "")
    }
});