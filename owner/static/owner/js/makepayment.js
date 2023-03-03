const pay_mode = document.querySelector('#payment_mode')
const utr_label = document.querySelector('#utr_label')
const utr = document.querySelector('#utr')
pay_mode.addEventListener('change', () => {
    if (pay_mode.value == "OF") {
        utr_label.style.display = "none";
        utr.style.display = "none";
    }
    if (pay_mode.value == "ON") {
        utr_label.style.display = "block";
        utr.style.display = "block";
    }
})

const pay_for = document.querySelector("#pay_for");
const desc_label = document.querySelector("#pay_desc");
const desc = document.querySelector("#desc")
desc_label.style.display = "none";
        desc.style.display = "none";
console.log(pay_for, desc, desc_label)
pay_for.addEventListener("change", ()=>{
    if(pay_for.value == "OB"){
        desc_label.style.display = "block";
        desc.style.display = "block";
    }else{
        desc_label.style.display = "none";
        desc.style.display = "none";
    }
})