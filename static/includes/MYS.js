const years = document.querySelector("#year");
for(let i = 2010; i < 2040; i++){
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