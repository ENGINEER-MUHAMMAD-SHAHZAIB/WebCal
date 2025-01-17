function append(value) {
    const expressionInput = document.getElementById("expression");
    expressionInput.value += value;
}

function clearDisplay() {
    document.getElementById("expression").value = "";
    document.getElementById("result").textContent = "0";
}

function backspace() {
    const expressionInput = document.getElementById("expression");
    expressionInput.value = expressionInput.value.slice(0, -1);
}

function calculate() {
    const expression = document.getElementById("expression").value;
    try {
        const result = eval(expression);
        document.getElementById("result").textContent = result;
    } catch (error) {
        document.getElementById("result").textContent = "Error";
    }
}
