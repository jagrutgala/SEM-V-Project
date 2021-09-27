function highlightPrase(index) {
    // console.log(index);
    let sentences= document.querySelector("#span-sentences").children;
    let clear_btn= document.querySelector("#clear-selection-btn");
    // console.log(clear_btn);
    for(let i=0; i<sentences.length; i++) {
        sentences[i].classList.remove("selected");
        if(index == i) {
            sentences[i].classList.add("selected");
        }
    }
    document.querySelector("#span-sentences").scrollIntoView({ block: "center", behavior: "smooth"});
    clear_btn.classList.remove("no-display");
}

function copyPhrase(index) {
    /* Get the text field */
    let question_li= document.querySelector("#questions--ul").children[index];
    // console.log(question_li);
    let copyText= question_li.querySelector(".question").innerHTML;
    console.log(copyText);
    navigator.clipboard.writeText(copyText);
}

function clearSelection() {
    let sentences= document.querySelector("#span-sentences").children;
    let clear_btn= document.querySelector("#clear-selection-btn");
    // console.log(sentences);
    for(let i=0; i<sentences.length; i++) {
        sentences[i].classList.remove("selected");
    }
    clear_btn.classList.add("no-display");
}

function toggleAnswer(indx) {
    console.log(indx);
    let clicked_li= document.querySelector("#questions--ul").children[indx];
    let ans_p= clicked_li.querySelector(".answer");
    console.log(clicked_li);
    if(ans_p.classList.contains("no-display")) {
        ans_p.classList.remove("no-display");
    } else {
        ans_p.classList.add("no-display");
    }
}

