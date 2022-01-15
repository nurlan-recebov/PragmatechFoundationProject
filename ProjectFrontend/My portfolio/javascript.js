// var btn =document.getElementById("btn")
// var slide = document.getElementById("slide")
// btn.onclick=function(){
//     slide.style.transform="translateX(800px)";
// }
let button = document.querySelector("#up")
console.log(button)
button.addEventListener('click',()=>{
    
    console.log("hjgh");
    window.scrollTo({ top: 0, behavior: 'smooth' });
    
})

document.getElementById("Home")=function(){
    
        document.getElementById("up").style.display="none"  

}