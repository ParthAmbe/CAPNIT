const display = document.getElementById("display");

document.querySelectorAll(".digit, .operator").forEach(button => {
    button.addEventListener("click", () => {
        display.value += button.getAttribute("data-value");
    });
});

document.getElementById("clear").addEventListener("click", () => {
    display.value = "";
});

document.getElementById("equals").addEventListener("click", () => {
    try {
        display.value = eval(display.value);
    } catch (error) {
        alert("Invalid Input");
        display.value = "";
    }
});
