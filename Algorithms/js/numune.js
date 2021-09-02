let arr = ['Xeyal', 'Selimov', 21]
    // index value cutluyu

let obj = {
    ad: 'Xeyal',
    soyad: 'Selimov',
    yas: 21
}


let obj2 = {
    ad: 'Ulvi',
    soyad: 'Hemidov',
    yas: 27
}


let obj3 = {
    ad: 'Elsen',
    soyad: 'Ceferov',
    yas: 24
}

class Corek {
    constructor(_un, _su) {
        this.un = _un
        this.su = _su
    }
}

function Foo() {
    let corek = new Corek('4kg un', '2 lt su')
    let corek2 = new Corek('12 kg un', '5lt su')
}
corek2.corekDetallariGoster()