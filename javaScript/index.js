const a = document.getElementById('1')
console.log(a)

const button = document.querySelector('.submit');
console.log("hello")
const order = document.getElementsByClassName('order').value;

console.log(order);

button.addEventListener("click", function(){
	console.log(order);
})