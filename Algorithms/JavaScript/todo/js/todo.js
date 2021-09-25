function removeElement(el){
    let silinecekOlanElement=el.parentElement
    let elementinAtasi=silinecekOlanElement.parentElement
    elementinAtasi.removeChild(silinecekOlanElement)

}

let yeniElement=`
<div class="input-group mb-3">
<input type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="basic-addon2">
<div class="btn btn-primary" onclick="removeElement(this)">Delete</div>
<div class="btn btn-primary" onclick="getData(this)">GetData</div>
</div>
`
function addNewElement(el){
    let esasDiv=el.parentElement.parentElement
    esasDiv.innerHTML+=yeniElement
}

function getData(el){
    if(el.parentElement.querySelector('input').value=='salam'){
        el.parentElement.style.border='1px solid red'
    }
}