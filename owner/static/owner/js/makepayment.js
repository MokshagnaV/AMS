const pay_mode = document.querySelector('#payment_mode')
const utr = document.querySelector('#utr-box')
const utrinput = document.querySelector("#utr");
pay_mode.addEventListener('change', () => {
    if (pay_mode.value == "OF") {
        utr.style.display = "none";
        utrinput.removeAttribute("required");
    }
    if (pay_mode.value == "ON") {
        utr.style.display = "flex";
        utrinput.setAttribute("required", "");
    }
})

const pay_for = document.querySelector("#pay_for");

const desc = document.querySelector("#pay_desc")
const desc_input = document.querySelector("#payment_desc");
desc.style.display = "none";


pay_for.addEventListener("change", ()=>{
    if(pay_for.value == "OB"){
        desc.style.display = "block";
        desc_input.setAttribute("required", "");
    }else{
        desc.style.display = "none";
        desc_input.removeAttribute("required");
    }
})

