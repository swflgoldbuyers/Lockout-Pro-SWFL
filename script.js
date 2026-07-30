// ================================
// MOBILE MENU
// ================================

const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector(".nav-links");

menuToggle.addEventListener("click", () => {
    navLinks.classList.toggle("active");
});

// Close menu after clicking a link

document.querySelectorAll(".nav-links a").forEach(link => {

    link.addEventListener("click", () => {

        navLinks.classList.remove("active");

    });

});

// ================================
// HEADER SHADOW
// ================================

const header = document.querySelector("header");

window.addEventListener("scroll", () => {

    if(window.scrollY > 40){

        header.style.boxShadow = "0 10px 30px rgba(0,0,0,.12)";

    }else{

        header.style.boxShadow = "0 5px 18px rgba(0,0,0,.05)";

    }

});

// ================================
// SCROLL REVEAL
// ================================

const observer = new IntersectionObserver((entries)=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            entry.target.style.opacity = "1";

            entry.target.style.transform = "translateY(0)";

        }

    });

},{
    threshold:.15
});

document.querySelectorAll(
".service-card, .why-card, .review-card, .area-card"
).forEach(card=>{

    card.style.opacity="0";

    card.style.transform="translateY(40px)";

    card.style.transition="all .6s ease";

    observer.observe(card);

});

// ================================
// ACTIVE NAVIGATION
// ================================

const sections = document.querySelectorAll("section[id]");
const navItems = document.querySelectorAll(".nav-links a");

window.addEventListener("scroll", ()=>{

    let current = "";

    sections.forEach(section=>{

        const top = section.offsetTop - 120;
        const height = section.clientHeight;

        if(pageYOffset >= top){

            current = section.getAttribute("id");

        }

    });

    navItems.forEach(link=>{

        link.classList.remove("active");

        if(link.getAttribute("href")==="#" + current){

            link.classList.add("active");

        }

    });

});
