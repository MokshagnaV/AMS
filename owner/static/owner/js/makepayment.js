const pay_mode = document.querySelector('#payment_mode')
const utr = document.querySelector('#utr')
pay_mode.addEventListener('change', () => {
    if (pay_mode.value == "OF") {
        utr.style.display = "none";
    }
    if (pay_mode.value == "ON") {
        utr.style.display = "flex";
    }
})

const pay_for = document.querySelector("#pay_for");

const desc = document.querySelector("#pay_desc")
desc.style.display = "none";

pay_for.addEventListener("change", ()=>{
    if(pay_for.value == "OB"){
        desc.style.display = "block";
    }else{
        desc.style.display = "none";
    }
})