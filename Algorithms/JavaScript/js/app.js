/* let ededler = [12, 45, 23, 67, 89, 1, 17, 90]
toplam = 0
for (let i = 0; i < 8; i++) {
    toplam = toplam + ededler[i]
}
console.log(toplam)
 */


/* let ededler = [12, 45, 23, 67, 89, 1, 17, 90];
for (let i = 0; i < 8; i++) {
    if (ededler[i] % 2 == 1) { console.log(`${ededler[i]} tek ededdir`) } 
    else { console.log(`${ededler[i]} cut ededdir`) };
} */

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

/* let ededler = [12, 45, 23, 67, 89, 1, 17, 90]   tapwiriq 1

for (let i = 0; i < 8; i++) {
    if (ededler[i] % 3 == 0 && ededler[i] % 5 != 0)
     { console.log(`${ededler[i]} 3 e bolunen 5 e bolunmeyen`) }
}
 */



/* let ededler = [12, 45, 23, 67, 89, 1, 17, 90];
toplam = 0
for (let i = 0; i < 8; i++) {
    toplam = toplam + ededler[2] % 10;
    ededler[2] = ededler[2] / 10
}
console.log(ededler[2]) */



/* let ededler = [12, 45, 23, 67, 89, 1, 17, 90]
toplam = 0
for (let i in ededler) {
    if (i % 2 == 0)
        toplam = toplam + ededler[i]
    console.log(ededler[i], i)

}
console.log(toplam) */




/* let ededler = [12, 45, 23, 67, 89, 1, 17, 90]  tapwiriq 4.
for (let i = 0; i < 8; i++) { if (ededler[i] % 10 == 7) { console.log(`${ededler[i]} sonu 7 olan`) } } */




/* let car = {
    name: "BMW",
    model: "F10",
    color: "black",
    start: function() {
        return this.name + " " + this.model + " isledi";
    },
    stop: function() {
        return this.name + " " + this.model + " dayandi";
    }
}
console.log(car.start())
console.log(car.stop()) */



/* function createDiv() {
    let div = document.createElement('div')
    div.style.width = '200px'
    div.style.height = '300px'
    div.style.background = 'red'
    div.style.margin = '10px'
    div.style.display = 'inline-block'
    div.addEventListener('click', function() {
        div.style.backgroundColor = 'green'

    })
    document.body.appendChild(div)
} */


/* for (let i = 0; i < 3; i++) {
    let div = document.createElement('div')
    div.style.width = '200px'
    div.style.height = '300px'
    div.style.background = 'red'
    div.style.display = 'inline-block'
    div.style.margin = '10px'
    document.body.appendChild(div)
} */



/* let btn = document.createElement("button")
btn.innerHTML = "click"
document.querySelector('.box').appendChild(btn)

btn.addEventListener('click', function() {
    document.querySelector(".box").style.backgroundColor = 'blue';

}); */