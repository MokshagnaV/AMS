const pay_mode = document.querySelector('#payment_mode')
        const utr_label = document.querySelector('#utr_label')
        const utr = document.querySelector('#utr')
        console.log(pay_mode, utr, utr_label)
        pay_mode.addEventListener('change', () => {
            if(pay_mode.value == "Offline"){
                utr_label.style.display = "none";
                utr.style.display = "none";
            }
            if(pay_mode.value == "Online"){
                utr_label.style.display = "block";
                utr.style.display = "block";
            }
        })