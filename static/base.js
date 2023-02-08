//Left sidebar
const body = document.getElementsByTagName('body')[0];
const burger = document.getElementsByClassName('hamburger-menu')[0];

burger.addEventListener("click", function () {
		$(this).toggleClass('open');
		//TODO: не работает - случается двойной клик
	// 	if ( body.classList.contains("darkened") ) {
	// 	body.classList.remove("darkened");
	// } else {
	// 	body.classList.add("darkened");
	// }
});
