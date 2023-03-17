const years = document.querySelector("#year");
const date = new Date();
const year = date.getFullYear();
for(let i = year; i > 2000; i--){
    const option = document.createElement("option");
    option.setAttribute("value", i);
    option.appendChild(document.createTextNode(i));
    years.appendChild(option);
}

get = document.querySelector("#get");
selects = document.querySelectorAll("select");  

get.addEventListener('click', (evt) => {   
    if (selects[0].value == "" || selects[1].value == ""){
        $('#validGet').modal('show')
        evt.preventDefault();
    }
})