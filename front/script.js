const typeWriterText = document.querySelector('.text-writer');
const textArr = ['Welcome\nto Machine Learning page', "Where we have\n outstanding projects", "That made us strong"];

let textArrayIndex = 0;
let charIndex = 0;

const type = () => {
    if(charIndex <= textArr[textArrayIndex].length - 1) {
        typeWriterText.textContent += textArr[textArrayIndex].charAt(charIndex);
        charIndex++
        setTimeout(type, 120);
    } else {
        setTimeout(erase, 800);
    }
}
const erase = () => {
    if(charIndex > 0) {
        typeWriterText.textContent = textArr[textArrayIndex].slice(0, charIndex - 1);
        charIndex--
        setTimeout(erase, 60);
    } else {
        textArrayIndex++;
        if(textArrayIndex >= textArr.length) {
            textArrayIndex = 0;
        }
        setTimeout(type, 800);
    }
}

//Starts animation on page load
document.addEventListener('DOMContentLoaded', () => {
    type()
})