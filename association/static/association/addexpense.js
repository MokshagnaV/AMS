let i = 1;

const add_item = () => {
    const main_div = document.createElement('div');
    main_div.classList.add("item");
    
    const item_div = document.createElement('div');
    const amount_div = document.createElement('div');

    const item_label = document.createElement('label')
    item_label.appendChild(document.createTextNode(`Item${i}`))
    item_label.setAttribute("for", `item${i}`)

    const item_input = document.createElement('input')
    item_input.setAttribute("type", "text")
    item_input.setAttribute("name", `expense${i}`)
    item_input.setAttribute("id", `item${i}`)
        

    item_div.appendChild(item_label)
    item_div.appendChild(item_input)

    const amount_label = document.createElement('label')
    amount_label.appendChild(document.createTextNode(`Amount${i}`))
    amount_label.setAttribute("for", `amount${i}`)

    const amount_input = document.createElement('input')
    amount_input.setAttribute("type", "number")
    amount_input.setAttribute("name", `amount${i}`)
    amount_input.setAttribute("id", `amount${i}`)

    amount_div.appendChild(amount_label)
    amount_div.appendChild(amount_input)

    main_div.appendChild(item_div)
    main_div.appendChild(amount_div)
    return main_div
}



const items = document.querySelector(".items");
const add = document.querySelector("#add");

add.addEventListener('click', () => {
    i++;
    items.appendChild(add_item());
})