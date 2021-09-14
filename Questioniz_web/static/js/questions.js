function highlightPrase(index) {
    // console.log(index);
    let sentences= document.querySelector("#span-text").children
    // console.log(sentences);
    for(let i=0; i<sentences.length; i++) {
        sentences[i].classList.remove("selected");
        if(index == i) {
            sentences[i].scrollIntoView();
            sentences[i].classList.add("selected");
        }
    }

}