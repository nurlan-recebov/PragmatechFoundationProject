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





    document.getElementById("sett").style.display = "block";
}

function seticon() {
    document.getElementById("settings").style.right = "50px"
    document.getElementById("sett").style.display = "block";

    document.getElementById("setbtn").disabled = true;
}

function purple() {
    const nodeList = document.querySelectorAll(".arxa,.container");
    for (let i = 0; i < nodeList.length; i++) {
        nodeList[i].style.backgroundColor = "purple";
    }
}

function yellow() {
    const nodeList = document.querySelectorAll(".arxa,.container");
    for (let i = 0; i < nodeList.length; i++) {
        nodeList[i].style.background = " #a337f6";
    }
}

function green() {
    const nodeList = document.querySelectorAll(".arxa,.container");
    for (let i = 0; i < nodeList.length; i++) {
        nodeList[i].style.backgroundColor = "green";
    }
}
// const element = document.getElementById("purple");

// element.addEventListener("click", function() {
//     document.querySelector('.arxa').style.backgroundColor = "purple"
// });