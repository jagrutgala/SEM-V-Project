var edit_area= document.querySelector("#text-area");
edit_area.addEventListener("input", function (event) {
    let words= edit_area.value.replace(/\n/g, " ").split(" ").filter((entry)=> {
        return entry.trim()!= '';
    });
    let no_of_words= words.length;
    edit_area.parentElement.setAttribute("words", no_of_words);
});


