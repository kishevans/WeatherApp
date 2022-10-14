document.getElementById('city-form').onsubmit = function (e) {
    e.preventDefault();
    fetch('/update', {
        method: 'POST',
        body: JSON.stringify({
            'city': document.getElementById('city').value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(jsonresponse){
        document.getElementById('city-name').innerHTML= jsonresponse['city']
        document.getElementById('weather-description').innerHTML= jsonresponse['weather']
        document.getElementById('day').innerHTML= jsonresponse['day']
        document.getElementById('icon').src= "http://openweathermap.org/img/wn/" + jsonresponse['icon'] + "@4x.png"
        document.getElementById('t').innerHTML= jsonresponse['temp'] 
        document.getElementById('time').innerHTML= jsonresponse['time'] 
    })
}



