"use strict";

const body = document.body;
const header = document.querySelector('.header')
const menuBurger = document.querySelector('.header__burger')


// Mobile menu
if (menuBurger) {
  menuBurger.onclick = function () {
    menuBurger.classList.toggle("open");
    header.classList.toggle("mobile-menu-opened");
  };
};


const coinBtn = document.querySelector('.coin-image');

coinBtn.addEventListener('click', function() {
  coinBtn.style.transform = 'scale(0.95)';

    setTimeout(function() {
      coinBtn.style.transform = 'scale(1)';
    }, 150)

});



const coinScaleElement = document.querySelector('.coin-scale');

const coinVal = 500;
const coinValInPerc = (coinVal / 9999) * 100;

function changeValue() {

}


function updateScale(value) {
  coinScaleElement.style.width = value + '%';
}