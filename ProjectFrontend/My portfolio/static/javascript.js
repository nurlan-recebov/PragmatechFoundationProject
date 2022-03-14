// var btn =document.getElementById("btn")
// var slide = document.getElementById("slide")
// btn.onclick=function(){
//     slide.style.transform="translateX(800px)";
// }
let button = document.getElementById("btn-back-to-top");

window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    if (
        document.body.scrollTop > 600 ||
        document.documentElement.scrollTop > 600
    ) {
        button.style.display = "block";
        button.style.zIndex = "99"
    } else {
        button.style.display = "none";
        button.style.zIndex = "-1"

    }
}

button.addEventListener("click", backToTop);

function backToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

function myFunction() {
    document.getElementById("menu").style.display = "block";
}

function nurlan() {
    document.getElementById("menu").style.display = "none";
}

function setbtn() {

    document.getElementById("settings").style.right = "290px"
    document.getElementById("setbt").disabled = true;

    document.getElementById("sett").style.display = "block";
}

function seticon() {
    document.getElementById("settings").style.right = "50px"
    document.getElementById("sett").style.display = "block";

}

function purple() {
    document.getElementsByClassName("arxa").style.backgroundColor = "purple"
    document.getElementsByClassName("container").style.backgroundColor = "purple"
}