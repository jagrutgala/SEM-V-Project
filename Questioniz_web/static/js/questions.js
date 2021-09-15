function highlightPrase(index) {
    // console.log(index);
    let sentences= document.querySelector("#span-text").children;
    let clear_btn= document.querySelector("#clear_selection-btn");
    console.log(clear_btn);
    for(let i=0; i<sentences.length; i++) {
        sentences[i].classList.remove("selected");
        if(index == i) {
            sentences[i].scrollIntoView();
            sentences[i].classList.add("selected");
        }

    }
    clear_btn.classList.remove("no-display");
    console.log(clear_btn.classList);
}


function clearSelection() {
    let sentences= document.querySelector("#span-text").children;
    let clear_btn= document.querySelector("#clear_selection-btn");
    // console.log(sentences);
    for(let i=0; i<sentences.length; i++) {
        sentences[i].classList.remove("selected");
    }
    clear_btn.classList.add("no-display");
}