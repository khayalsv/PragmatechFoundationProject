function changeimage(elem) {
    let thumbimage = elem.querySelector('img').getAttribute('src')
    document.querySelector('.images-frame img').setAttribute('src', thumbimage)


}