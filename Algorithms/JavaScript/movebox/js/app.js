var qutu = document.querySelector(".box");
var x = 0;
var y = 0;


function pos() {

    var kordinat = document.getElementById('.box').getBoundingClientRect(), //objeye erişiyoruz ve pozisyon bilgilerini alıp konum değişkenine atıyoruz

        left = Math.round(kordinat.left), //objenin solda ne kadar uzak olduğunu alıyoruz

        top = Math.round(kordinat.top); //objenin yukarıdan uzaklığını alıyoruz.


}



window.onkeydown = function(event) {
    switch (event.keyCode) {
        //sol
        case 37:
            x -= 2;
            qutu.style.left = x + "px";
            break;
            //sag
        case 39:
            x += 2;
            qutu.style.left = x + 'px';
            break;
            //yuxari
        case 38:
            y -= 2;
            qutu.style.top = y + 'px';
            break;
            //asagi
        case 40:
            y += 2;
            qutu.style.top = y + 'px';
            break;
    }
}

console.log(x, y)