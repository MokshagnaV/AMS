let i = 1;

const add_item = () => {
    let main_div = document.createElement("div");
    main_div.classList.add("items", "form-group", "row")
    main_div.setAttribute("id", `item-box${i}`);
    main_div.innerHTML = `
        <div class="col">
            <label for="item${i}">Item <span class="required">*</span></label>
            <input type="text" class="form-control" name="expense${i}" id="item${i}" required>
        </div>
        <div class="col">
            <label for="amount${i}">Amount <span class="required">*</span></label>
            <input type="number" class="form-control" name="amount${i}" id="amount${i}" required>
        </div>
        <div class="del btn btn-inverse-danger btn-sm" onclick="delete_ele(this)" >Delete</div>
`
    return main_div
}



const items = document.querySelector(".form");
const add = document.querySelector("#add");
add.addEventListener('click', () => {
    i++;
    items.appendChild(add_item());
})

const delete_ele = (e) => {
    
    e.parentElement.outerHTML= "";
}