const events = document.querySelectorAll('.event')
const button = document.querySelector('#scroll_back')
const display = document.querySelectorAll('.display')


/* redirect to dynamic url*/
events.forEach(event => {
    event.addEventListener('click', () => {
        const name = event.getAttribute('data-value');
        window.location.href = name;
    })
})



/* Gsap Animations */
gsap.registerPlugin(ScrollTrigger);

button.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
    })
})

gsap.from(display, {
    x: 200,
    duration: .7,
    ease: "ease",
    stagger: 0.3
})

gsap.from(button, {
    scrollTrigger: button, 
    start: "bottom bottom",
    x: 200,
    duration: .9,
    ease: "back.out(2.5)",
});