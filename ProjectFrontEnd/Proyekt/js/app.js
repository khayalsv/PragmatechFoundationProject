let cursor = document.querySelector('.cursor')
let cursor2 = document.querySelector('.cursor2')
document.addEventListener("mousemove", function(el) {
    cursor.style.left = cursor2.style.left = el.pageX + 'px'
    cursor.style.top = cursor2.style.top = el.pageY + 'px'

})