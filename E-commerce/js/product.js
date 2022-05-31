//Number of Quantity user wants
var increase = document.getElementById('increaseQuantity');
var decrease = document.getElementById('decreaseQuantity');
var num = document.getElementById('num');

//increases the value
increase.addEventListener("click", function() {
    console.log('Increase Invoke');
    console.log(num.textContent);
    num.textContent = Number(num.textContent) + 1
})

//decreases the value
decrease.addEventListener("click", function() {
    console.log('Decrease Invoke');
    console.log(num.textContent);
    if (num.textContent == Number(0)) {
        num.textContent = 0;
    } else {
        num.textContent = Number(num.textContent) - 1
    }
})

// Swiper