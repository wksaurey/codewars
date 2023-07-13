decode = (input_string) => {
    result = Array.from(input_string, char => '5987604321'[Number(char)]).join("");
    console.log(result);
    return result;
}

const input = document.getElementById('text-input');
const originalInput = document.getElementById('original-input');

input.addEventListener("focus", () => {
    input.value = '';
})
input.addEventListener("blur", () => {
    displayCode();
        input.value = '';
})
input.addEventListener("keydown", (e) => {
    if(e.key === 'Enter') {
        displayCode();
        input.value = '';
        // input.blur();
    }
});


function displayCode() {
    if(input.value == null) input.value = '';
    console.log(input.value)
    originalInput.textContent = decode(input.value);
}