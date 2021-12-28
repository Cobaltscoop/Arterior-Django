import '../example/food/style.css';
import './food/nmap'

/* https://raw.githubusercontent.com/bedimcode/responsive-portfolio-website-JhonDoe/master/assets/js/main.js
=====*/


/* === (모바일) Navigation : 메뉴 슬라이드  === */
/* 1) Show & Hide the Menu */
const showMenu = (toggleId, navId) =>{
	const toggle = document.getElementById(toggleId);
	const nav = document.getElementById(navId);
	if(toggle && nav){
		toggle.addEventListener('click', ()=>{
			nav.classList.toggle('show-menu')
		})
	}
}
showMenu('nav-toggle','nav-menu');


/* === (모바일) Navigation 의 Link 클릭시 추가 Event  === */
/* 1) Hide the Menu 2 : .nav__link 를 클릭했을 때, 자동 숨기기 */
const navLink = document.querySelectorAll('.nav__link');
function linkAction(){
	const navMenu = document.getElementById('nav-menu');
	navMenu.classList.remove('show-menu');
}
navLink.forEach(n => n.addEventListener('click', linkAction));

/* 2) Hide the Menu 2 : .nav__link 를 클릭했을 때, ACTIVE LINK 속성 제거 */
const sections = document.querySelectorAll('section[id]')
function scrollActive(){
	const scrollY = window.pageYOffset
	sections.forEach(current =>{
		const sectionHeight = current.offsetHeight
		const sectionTop = current.offsetTop - 50;
		sectionId = current.getAttribute('id')
		if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
			document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.add('active')
		}else{
			document.querySelector('.nav__menu a[href*=' + sectionId + ']').classList.remove('active')
		}
	})
}
window.addEventListener('scroll', scrollActive)


/* === (모바일 & Scroll) Navigation : Header 그림자 생성함수 === */
function scrollHeader(){
	const nav = document.getElementById('header')
	// When the scroll is greater than 200 viewport height
	if(this.scrollY >= 200) nav.classList.add('scroll-header'); else nav.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)


/* === (Scroll) ScrollTop 이동 버튼 === */
function scrollTop() {
	const scrollTop = document.getElementById('scroll-top');
	// Scroll 을 560px 이상 움직였을 때
	// <header> 에 "scroll-header" 속성(그림자 효과) 을 추가 한다
	if(this.scrollY >= 560) scrollTop.classList.add('scroll-top');
	else scrollTop.classList.remove('scroll-top');
}
window.addEventListener('scroll', scrollTop)


/* === (Theme ) Light/Dark Theme button === */
const themeButton = document.getElementById('theme-button');
const darktheme = 'dark-theme';
const icontheme = 'fa-moon';
const iconthemeorg = 'fa-sun';
// Activate/Deactivate the Theme (Add or Remove the dark Theme)
themeButton.addEventListener('click', ()=>{
	document.body.classList.toggle(darktheme);
	themeButton.classList.toggle(iconthemeorg);
	themeButton.classList.toggle(icontheme);
})

/* Scroll the Reveal Animation 
Animate On Scroll MIT licence..
https://michalsnik.github.io/aos/
*/