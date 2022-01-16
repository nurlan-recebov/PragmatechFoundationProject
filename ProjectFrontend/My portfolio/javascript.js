// var btn =document.getElementById("btn")
// var slide = document.getElementById("slide")
// btn.onclick=function(){
//     slide.style.transform="translateX(800px)";
// }
let button = document.querySelector("#up")
let right = document.querySelector(".right")
let shadow = document.querySelector(".shadow")

button.addEventListener('click',()=>{
    

    window.scrollTo({ top: 0, behavior: 'smooth' });
    
})



