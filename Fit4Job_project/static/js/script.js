const signInBtn = document.getElementById("signIn");
const signUpBtn = document.getElementById("signUp");
const fistForm = document.getElementById("form1");
const secondForm = document.getElementById("form2");
const container = document.querySelector(".container");

signInBtn.addEventListener("click", () => {
  container.classList.remove("right-panel-active");
});

signUpBtn.addEventListener("click", () => {
  container.classList.add("right-panel-active");
});

fistForm.addEventListener("submit", (e) => e.preventDefault());
secondForm.addEventListener("submit", (e) => e.preventDefault());


$(document).ready(function(){
  var li = $('li');
  TweenMax
    .staggerTo(li, 0.25, {css: {opacity: "1", display:"block"}}, 0.25);  
    //.from(a, 2, {autoAlpha: 0});
    //.from(h3, 2, {autoAlpha: 0});
});







