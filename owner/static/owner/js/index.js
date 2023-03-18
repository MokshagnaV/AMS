const API_KEY = `3265874a2c77ae4a04bb96236a642d2f`
    // const API = `https://api.openweathermap.org/data/2.5/weather?
    // q=${city}&appid=${API_KEY}&units=metric`
    // const IMG_URL = `https: //openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`
const weather = document.querySelector("#weather");
findLocation= () => {
    const success = (position) => {
        console.log(position)
        const lat = position.coords.latitude
        const lon = position.coords.longitude
        getWeather(lat, lon)
    }
    const error = () => {
        weather.innerHTML = "<div style='max-width: 200px'><p class='muted'>Allow Location Permissions to get Live Weather Info.</p></div>";
    }
    navigator.geolocation.getCurrentPosition(success, error)
}

document.addEventListener("DOMContentLoaded", () => {
    findLocation();
})
const getWeather = async(lat, lon) => {
    weather.innerHTML = `<h2> Loading... <h2>`
    const url1 = `http://api.openweathermap.org/geo/1.0/reverse?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
    const response1 = await fetch(url1);
    const data1 = await response1.json()
    console.log(data1)
    city = data1[0]
    const url2 = `https://api.openweathermap.org/data/2.5/weather?q=${city.name}&appid=${API_KEY}&units=metric`;
    const response2 = await fetch(url2);
    const data = await response2.json()
    return showWeather(data, city)
}

const showWeather = (data, city) => {
    if (data.cod == "404") {
        weather.innerHTML = `<h2> City Not Found <h2>`
        return;
    }
    weather.innerHTML = `
        <div class="d-flex">
                <div>
                  <h4 class="mb-0 font-weight-normal"><img src="https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png" style="width: 40px">${data.main.temp}℃</h4>
                </div>
                <div class="ml-2">
                  <h4 class="location font-weight-normal">${city.name}, <span>${city.country}</span></h4>
                  <h4 class="location font-weight-normal">${city.local_names.te}</h4>
                </div>
        </div>
    `
}