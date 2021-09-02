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

/* let ededler = [12, 45, 23, 67, 89, 1, 17, 90]   tapwırıq 1

for (let i = 0; i < 8; i++) {
    if (ededler[i] % 3 == 0 && ededler[i] % 5 != 0) { console.log(`${ededler[i]} 3 e bolunen 5 e bolunmeyen`) }
}
 */



/* let ededler = [12, 45, 23, 67, 89, 1, 17, 90];
toplam = 0
for (let i = 0; i < 8; i++) {
    toplam = toplam + ededler[2] % 10;
    ededler[2] = ededler[2] / 10
}
console.log(ededler[2]) */



let ededler = [12, 45, 23, 67, 89, 1, 17, 90]
toplam = 0
for (let i = 0; i < ededler.length; i++) {
    if (i % 2 == 0)
        toplam = toplam + ededler[i]

}
console.log(toplam)



/* let ededler = [12, 45, 23, 67, 89, 1, 17, 90]  tapwiriq 4.
for (let i = 0; i < 8; i++) { if (ededler[i] % 10 == 7) { console.log(`${ededler[i]} sonu 7 olan`) } } */