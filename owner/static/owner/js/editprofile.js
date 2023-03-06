function showPreview(event) {
  if (event.target.files.length > 0) {
    let src = URL.createObjectURL(event.target.files[0]);
    let preview = document.getElementById("pic-preview");
    preview.src = src;
    preview.style.display = "block";
  }
}

const getOptions = (floor) => {
  floor_num = floor.value;
  if (floor_num == 0) floor_num = "G";
  const flat = document.querySelector("#flat-num");
  flat.innerHTML = "";
  for (let i = 1; i < 7; i++) {
    const option = document.createElement("option");
    option.setAttribute("value", `${floor_num}0${i}`);
    option.appendChild(document.createTextNode(`${floor_num}0${i}`));
    flat.appendChild(option);
  }
};

const floor = document.querySelector("#floor-num");
floor.addEventListener("change", () => {
  getOptions(floor);
});
