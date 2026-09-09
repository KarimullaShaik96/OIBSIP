function convertTemperature() {
const temperatureInput = document.getElementById("temperature");
const unit = document.getElementById("unit").value;
const result = document.getElementById("result");

```
const temperature = parseFloat(temperatureInput.value);

// Validate empty or invalid input
if (isNaN(temperature)) {
    result.textContent = "Please enter a valid temperature.";
    return;
}

// Absolute zero validation
if (unit === "celsius" && temperature < -273.15) {
    result.textContent = "Temperature cannot be below absolute zero.";
    return;
}

if (unit === "fahrenheit" && temperature < -459.67) {
    result.textContent = "Temperature cannot be below absolute zero.";
    return;
}

if (unit === "kelvin" && temperature < 0) {
    result.textContent = "Kelvin cannot be below 0 K.";
    return;
}

let celsius;
let fahrenheit;
let kelvin;

// Convert input to Celsius first
if (unit === "celsius") {
    celsius = temperature;
} else if (unit === "fahrenheit") {
    celsius = (temperature - 32) * 5 / 9;
} else if (unit === "kelvin") {
    celsius = temperature - 273.15;
}

// Convert Celsius to all units
fahrenheit = (celsius * 9 / 5) + 32;
kelvin = celsius + 273.15;

result.innerHTML = `
    <div>
        <p>Celsius: ${celsius.toFixed(2)} °C</p>
        <p>Fahrenheit: ${fahrenheit.toFixed(2)} °F</p>
        <p>Kelvin: ${kelvin.toFixed(2)} K</p>
    </div>
`;
```

}
