import './test.css';
// import "../home/style.css";

// Navigation : Menu Auto Hide
var lastScrollTop = 0;
var navbar = document.getElementById("navbar");
window.addEventListener("scroll", function(){
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if (scrollTop > lastScrollTop){
        navbar.style.top='-80px';
    } else {
        navbar.style.top="0";
    }
    lastScrollTop = scrollTop;
})


$(function() {
    let start = 0;
    let end = $(".num").html();
    let speed = 10;

    setInterval(function(){
        if(start<end){
            start++;
        }
        $(".num").html(start);
    }, speed);
});